from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    created_date_time = models.DateTimeField('date created')
    updated_date_time = models.DateTimeField('date updated')

class Department(models.Model):
    department_id = models.IntegerField('unique id')
    name = models.CharField(max_length=50)