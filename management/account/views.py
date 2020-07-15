from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import (CreateAPIView,)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import (ManagerRegistrationSerializer,ManagerJWTTokenSerializer)
from .models import Manager
# Create your views here.
class ManagerRegisterView(CreateAPIView):
    '''
     create new Manager 
     
     '''
    serializer_class = ManagerRegistrationSerializer
    permission_classes = (AllowAny,)
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
           'success' :'True',
           'massage' : ' Manager Register Successfully'      
            }
        except Exception as e :
            return Response({'Please check the fields {}'.format(e)
            })
        return Response(response,status = status_code)

class ManagerJWTToken(APIView):
    permission_classes =[AllowAny]
    serializer_class = ManagerJWTTokenSerializer
    def post(self,request):
        try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception=True)
            response = {
            'success' : 'True',
            'statuscode' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            
            }
            status_code =status.HTTP_200_OK
        except Exception as e :
            return Response({'Manager Failed to login{}'.format(e)
            })
        return Response(response,status_code)