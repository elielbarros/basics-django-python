from django.shortcuts import render
from blog.data import posts
import requests

# Create your views here.


def blog(request):
    # It works but is very slow
    # response = requests.get('https://jsonplaceholder.typicode.com/posts')
    # json_content = response.json()
    context = {
        # 'text': 'You are in blog page.',
        'title': 'Blog Title - ',
        'posts': posts
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
