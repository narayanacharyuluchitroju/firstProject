from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>My first Django App</h1>")

def displayDateTime(request):
    s = "<b>Current date and time : </b>"+str(datetime.datetime.now())
    return HttpResponse(s)

