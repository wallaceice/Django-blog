from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.


def game(request):
    return render(request, 'game.html', {})
