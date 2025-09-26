
from django.shortcuts import render
from django.urls import path


# Create your views here.


def index(request):
    context = {
        'text': 'Pagina Inicial',
        'title': 'Pagina inicial - '
    }

    return render(
        request,
        'home/index.html',
        context,

    )
