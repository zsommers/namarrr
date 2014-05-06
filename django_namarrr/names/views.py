from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

    message_list = messages.get_messages(request)
    for message in message_list:
        if message.level == messages.SUCCESS:
            message.alert_class = " alert-success"
        elif message.level == messages.INFO:
            message.alert_class = " alert-info"
        elif message.level == messages.WARNING:
            message.alert_class = " alert-warning"
        elif message.level == messages.ERROR:
            message.alert_class = " alert-danger"

    return render(request,
                  'names/index.html',
                  context)


@login_required
def upvote(request, model_id, model):
    word = model.objects.get(pk=model_id)
    word.upvote(request.user)

    messages.success(request, "You voted for {}".format(word.text))

    return redirect('names:index')


@login_required
def downvote(request, model_id, model):
    word = model.objects.get(pk=model_id)
    word.upvote(request.user)

    messages.success(request, "You voted against {}".format(word.text))

    return redirect('names:index')
