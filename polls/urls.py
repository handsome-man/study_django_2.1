# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView, name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView, name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView, name='results'),
    # ex: /polls/5/vote/
    path('<int:pk>/vote/', views.vote, name='vote'),
]
