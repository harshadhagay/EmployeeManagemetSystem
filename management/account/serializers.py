from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from  rest_framework_jwt.settings import api_settings
from . models import Manager

# Manager pass as payload and encode manager data
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class ManagerRegistrationSerializer(serializers.ModelSerializer):
    ''' 
        Serialize Manager model and 
        adding validation Manager model
    '''
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     style={
                                    'input_type':'password'
                                    })
    confirm_password = serializers.CharField(write_only=True,
                                      label='Confirm Password',
                                      style= {'input_type':'password'})
    class Meta:
        model = Manager
        fields = [
                    'email',
                    'password',
                    'confirm_password',
                    'firstname',
                    'lastname',
                    'address',
                    'date_of_birth',
                    'company',
                   
                ]
    # create manager 
    def create(self,validated_data):
        manager = Manager.objects.create(
            email = validated_data['email'],
            firstname = validated_data['firstname'],
            lastname =validated_data['lastname'],
            password = validated_data['password'],
            address = validated_data['address'],
            date_of_birth = validated_data['date_of_birth'],
            company = validated_data['company']
        )
        return manager
    
class ManagerJWTTokenSerializer(serializers.Serializer):
    ''' 
    Manager Login serializer used generate token
    
    '''
    email = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length=128, 
                                     write_only=True,
                                     style= {'input_type':'password'})
    token = serializers.CharField(max_length=255, 
                                  read_only=True)
    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        manager = authenticate(email=email, password=password)
        if manager is None :
            raise serializers.ValidationError(
                'Manager with this mail id is not exist'
            )
        try :
            payload = JWT_PAYLOAD_HANDLER(manager)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            
            update_last_login(None,manager)
        except Manager.DoesNotExist:
            raise serializers.ValidationError(
                'Manager with this email id and password doesnot exist'
            )
        return {
            'email' : manager.email,
            'token' : jwt_token
        }
        
class ManagerSerializer(serializers.ModelSerializer):
    '''
        Manager Serializer use in employee relation
    '''
    # manager_employee = EmployeeSerializer(many=True)
    
    class Meta:
        model = Manager
        fields = ('email',)
    
    
           
            
        
        
        
    
    