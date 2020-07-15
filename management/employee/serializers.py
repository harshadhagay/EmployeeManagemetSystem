from rest_framework import serializers
from account.models import Manager
from account.serializers import ManagerSerializer
from . models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    
    ''' Employee Serializer '''
    
    
    manager = ManagerSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = (
                'manager',
                'email',
                'firstname',
                'lastname',
                'address',
                'date_of_birth',
                'city',
                'phonenumber',
                  )
        read_only_fields = ('manager')
    def create(self,validated_data):
       manager =validated_data.pop('email')
       employee = Employee.objects.create(**validated_data)
       return employee
      
        
    
    