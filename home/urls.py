from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.login, name='login'),
    path("Registration/", views.Registration, name='Registration'),
    path("appointment/", views.appointment, name='appointment'),
    path("treatment/", views.treatment, name='treatment'),
    path("events/",views.events, name='events'),
    path("health/", views.health, name='health'),
    path("forgotpass/", views.forgotpass, name='forgotpass')
]