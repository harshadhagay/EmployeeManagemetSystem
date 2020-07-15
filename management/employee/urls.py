from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import (CreateEmployee,GetEmployeeDetails,ModifyEmployeeDetails,)


router = DefaultRouter()
urlpatterns = [
    path('employee/create/',CreateEmployee.as_view(),name='create employee'),
    path('employee/details/',GetEmployeeDetails.as_view(),name ='Employee Details'),
    path('employee/update/<int:id>',ModifyEmployeeDetails.as_view(),name =' Update Employee'),
  
]