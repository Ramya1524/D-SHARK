from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def homePage(reqest):
    
    return HttpResponse("Hello Developer!")
    
    