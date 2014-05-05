from random import uniform

from django.db import models


class WordManager(models.Manager):
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
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=16,
                                 decimal_places=15,
                                 default=5)

    def upvote(self):
        """Business logic for handling upvotes"""
        self.upvotes += 1
        self.weigh_votes()

    def downvote(self):
        """Business logic for handling downvotes"""
        self.downvotes += 1
        self.weigh_votes()

    def weigh_votes(self):
        """Logic for weighting Word votes"""
        votes = abs(self.upvotes - self.downvotes)
        offset = 100 / (votes + 20)
        if self.upvotes > self.downvotes:
            self.weight = 5 + offset
        else:
            self.weight = 5 - offset

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
