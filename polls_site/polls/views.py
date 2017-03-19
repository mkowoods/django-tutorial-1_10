from django.shortcuts import render, get_object_or_404, reverse
#from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Question, Choice

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request=request, template_name='polls/index.html', context=context)

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s."%question_id)
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', context={
            'question': question,
            'error_message': "You didnt select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', kwargs={'question_id': question.id}))



