from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404
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


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post does not exist.')
    
    context = {
        'title': found_post['title'],
        'post': found_post
    }
    
    return render(
            request,
            'blog/post.html',
            context
    )
