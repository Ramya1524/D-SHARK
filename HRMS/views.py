from django.shortcuts import render
from django.template import loader
from datetime import datetime
from HRMS import models
from django.views.generic import CreateView
from .models import Employee
from .forms import LoginForm

# Create your views here.
from django.http import HttpResponse

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ('employee_id','name','created_date_time','updated_date_time')


def homePage1(reqest):
    template = loader.get_template('HRMS/login.html')
    
    context = {"name":"D-Shark"}
    #form = Employee()
    #return render(reqest,'HRMS/login.html')
    #return render(reqest,'HRMS/login.html',{'form': form})
    return HttpResponse(template.render(context,reqest))
    

def homePage(request):
    # if this is a POST request we need to process the form data
    #if request.method == 'POST':
        # create a form instance and populate it with data from the request:
    form = LoginForm()
        # check whether it's valid:
       # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
           # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    #else:
        #form = LoginForm()

    return render(request, 'HRMS/login.html', {'form': form})