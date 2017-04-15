from django.http import HttpResponse
from django.shortcuts import render
from elo import templates


def index(request):
    return render(request, 'angularui/index.html')
