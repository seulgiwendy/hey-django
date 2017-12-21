from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    q = Question.objects.get(pk = question_id)
    return render(request, "polls/detail.html", {'question' : q})

def results(request, question_id):
    response = "Question id : %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vote Page : %s" % question_id)

