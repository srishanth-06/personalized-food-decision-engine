from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('meal/', views.meal_input, name='meal_input'),
    path('result/', views.result, name='result'),
]
