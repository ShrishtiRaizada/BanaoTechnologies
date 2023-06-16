
from django.urls import path
from app import views

urlpatterns = [
    path('', views.Login, name="login"),
    path('signup/', views.SignUp, name="Signup"),
    path('home/',views.patient,name="patient")

]
