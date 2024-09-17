from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index.html'),
    path('add_employee/',views.add_employee,name='add_employee'),
    path('employee_list',views.employee_list,name='employee_list'),
    path('search',views.searching,name='search'),
]