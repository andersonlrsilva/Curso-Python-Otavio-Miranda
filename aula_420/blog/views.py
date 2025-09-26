
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from blog.data import posts


# Create your views here.
def blog(request):

    context = {
        'text': 'Pagina do Blog',
        'title': 'Pagina do blog - ',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post(request, id):
    context = {

        'posts': posts,
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


def exemplo(request):
    context = {
        'text': 'Pagina de exemplo',
        'title': 'Pagina de Exemplo - '
    }

    return render(
        request,
        'blog/exemplo.html',
        context,
    )
