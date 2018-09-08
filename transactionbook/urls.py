from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datacount/', views.datacount, name='datacount'),
    path('datacount1/', views.datacount1, name='datacount1'),
    path('summaryresults/', views.summaryresults, name='summaryresults'),
]
