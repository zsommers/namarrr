from django.shortcuts import render

from names.models import Adjective, Noun, Surname


def index(request):
    """Main page showing name"""
    context = {
        'adjective': Adjective.objects.weighted_random(),
        'noun': Noun.objects.weighted_random(),
        'surname': Surname.objects.weighted_random()
    }

    return render(request,
                  'names/index.html',
                  context)
