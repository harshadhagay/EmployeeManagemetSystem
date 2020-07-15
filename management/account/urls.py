from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (ManagerRegisterView,
                    ManagerJWTToken,)

router = DefaultRouter()

urlpatterns = [
    path('manager/register', ManagerRegisterView.as_view(),name= 'ManagerRegister'),
    path('token/', ManagerJWTToken.as_view() , name='TokenAuthentication'),
]
