
from django.urls import path
from .views import *
urlpatterns = [
    path('',Employees.as_view()), 
    path('employees/<int:pk>/',EmployeesDetail.as_view()),#class based view 
]