from django.shortcuts import render

from names.models import Adjective, Noun, Surname


def index(request):
    """Main page showing name"""
    adjective = Adjective.objects.weighted_random()
    noun = Noun.objects.weighted_random()
    surname = Surname.objects.weighted_random()

    context = {
        'adjective': adjective,
        'noun': noun,
        'surname': surname,
    }

    if request.user.is_authenticated():
        if adjective in request.user.adjective_upvotes.all():
            context['adjective_upvote'] = True
        elif adjective in request.user.adjective_downvotes.all():
            context['adjective_downvote'] = True
        if noun in request.user.noun_upvotes.all():
            context['noun_upvote'] = True
        elif noun in request.user.noun_downvotes.all():
            context['noun_downvote'] = True
        if surname in request.user.surname_upvotes.all():
            context['surname_upvote'] = True
        elif surname in request.user.surname_downvotes.all():
            context['surname_downvote'] = True

    return render(request,
                  'names/index.html',
                  context)
