from django.urls import path
from . import views

urlpatterns = [
    path('', views.goals),
    path('game', views.index),
    path('process_money', views.process_money),
    path('reset', views.reset),
    path('process', views.process),
]