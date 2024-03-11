from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog(request):
    # do something here
    return HttpResponse('Blog Views')


def example(request):
    return HttpResponse('Example View')
