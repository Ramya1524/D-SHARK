from django.urls import path
from HRMS import views

urlpatterns=[
    path("", views.homePage, name="homePage"),
]