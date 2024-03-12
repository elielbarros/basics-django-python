from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog(request):
    context = {
        'text': 'You are in blog page.',
        'title': 'Blog Title - '
    }
    
    return render(
            request,
            'blog/index.html',
            context
    )


def example(request):
    context = {
        'text': 'You are in example page.',
        'title': 'Example Title - '
    }
    
    return render(
            request,
            'blog/example.html',
            context
    )
