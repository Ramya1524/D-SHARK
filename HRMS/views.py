from django.shortcuts import render
from django.template import loader
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def homePage(reqest):
    template = loader.get_template('HRMS/login.html')
    
    context = {"name":"D-Shark"}
    #return render(reqest,'HRMS/login.html')
    return HttpResponse(template.render(context,reqest))
    
    