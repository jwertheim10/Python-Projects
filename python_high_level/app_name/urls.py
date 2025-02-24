from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),  
    path('add/<int:num1>/<int:num2>', views.add, name='add'),
    path('operation/', views.operation, name='operation'),
    path('sum_multiples/', views.sum_multiples, name = 'sum_multiples'),
    path('form/', views.form, name = 'form')
    ]