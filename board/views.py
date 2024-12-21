from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards})


# def boards_topics(request, pk):
#     board = Board.objects.get(pk=pk)
#     # return HttpResponse("Hello world!" + id)
#     return render(request, 'topics.html', {'board':board})