from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'BrianGL',
        'title': 'Blog Post 01',
        'content': 'Post 01 content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'AngleaGL',
        'title': 'Blog Post 02',
        'content': 'Post 02 content',
        'date_posted': 'August 27, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
