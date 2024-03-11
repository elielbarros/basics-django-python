from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    # do something here
    return HttpResponse('Home View')
