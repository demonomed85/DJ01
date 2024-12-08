from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Это мой первый проект Django!')

def data(request):
    return HttpResponse('Это страница data!')

def test(request):
    return HttpResponse('Это страница test!')
# Create your views here.