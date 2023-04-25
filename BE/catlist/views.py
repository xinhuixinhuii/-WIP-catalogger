from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("You are at the cat list.")

def detail(request, catListName):
    return HttpResponse("You are looking at catListName %s." % catListName)
