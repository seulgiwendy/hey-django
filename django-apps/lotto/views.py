from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from lotto.models import GuessNumbers


def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, "./lotto/default.html", {"lottos" : lottos})



