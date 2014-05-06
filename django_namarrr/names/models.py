from random import uniform

from django.db import models
from django.conf import settings


class WordManager(models.Manager):
    """Custom Manager to add selection of weighted random word"""
    def weighted_random(self, **kwargs):
        total = self.aggregate(models.Sum('weight'))['weight__sum']
        pick = uniform(0, float(total))
        sum = 0
        for word in self.all():
            sum += word.weight
            if sum > pick:
                return word


class Word(models.Model):
    """Abstract base model of rateable words"""
    text = models.CharField(max_length=64,
                            unique=True)
    upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='%(class)s_upvotes')
    downvotes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='%(class)s_downvotes')
    weight = models.DecimalField(max_digits=16,
                                 decimal_places=15,
                                 default=5)

    def upvote(self, user):
        """Business logic for handling upvotes"""
        self.upvotes.add(user)
        self.weigh_votes()
        self.save()

    def downvote(self, user):
        """Business logic for handling downvotes"""
        self.downvotes.add(user)
        self.weigh_votes()
        self.save()

    def weigh_votes(self):
        """Logic for weighting Word votes"""
        votes = float(abs(self.upvotes.count() - self.downvotes.count()))
        offset = 100.0 / (votes + 20.0)
        if self.upvotes.count() > self.downvotes.count():
            self.weight = 10.0 - offset
        else:
            self.weight = 0.0 + offset

    def __str__(self):
        return self.text

    class Meta:
        abstract = True

    objects = WordManager()


class Adjective(Word):

    def __repr__(self):
        return "<Adjective: text: {}, weight: {}>".format(self.text,
                                                          self.weight)


class Noun(Word):

    def __repr__(self):
        return "<Noun: text: {}, weight: {}>".format(self.text,
                                                     self.weight)


class Surname(Word):

    def __repr__(self):
        return "<Surname: text: {}, weight: {}>".format(self.text,
                                                        self.weight)
