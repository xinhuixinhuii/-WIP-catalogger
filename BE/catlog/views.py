from django.shortcuts import render
from django.http import HttpResponse
from .models import CatLog


def index(request):
    return("You are viewing the cat logs for the day.")

def detail(request, catLogName):
    return HttpResponse("You are looking at catLogName %s." % catLogName)

def result(request, catLogName, dateTime):
    log = "This catLogName %s is reported at."
    return HttpResponse(log % dateTime)

