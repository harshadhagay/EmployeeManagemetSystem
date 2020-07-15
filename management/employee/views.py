from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from . serializers import EmployeeSerializer
from . models import Employee



# Create your views here.
class CreateEmployee(APIView):
    '''Creatr Employee for manager '''
    permission_classes = [IsAuthenticated]
    # employee_serializer = EmployeeSerializer
    def post(self,request):
        try:
            # manager1 = Manager.objects.get(email = request.manager).prefetch_related('manager_employee')
            # emp = manager1.manager_employee
            # print(emp)
            employeedata = EmployeeSerializer(data = request.data)
            employeedata.is_valid(raise_exception=True)
            employeedata.save()
        except Employee.DoesNotExist:
            return Response({'message':'Employee not created,check employee data'},status=status.HTTP_400_BAD_REQUEST)
            
        return Response(employeedata.data,status=status.HTTP_201_CREATED)
    
   
class GetEmployeeDetails(APIView):
    ''' 
        Get All Employee details 
    '''
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        try:
            employee_list = Employee.objects.all()
            employeeserializer = EmployeeSerializer(employee_list,many=True)
        except Exception as e:
            return Response({'Employess data{}'.format(e)})
        return Response(employeeserializer.data,status=status.HTTP_200_OK)
    
class ModifyEmployeeDetails(APIView):
    
    ''' 
    Get perticular employee detail and modify employee data
    
    '''
    permission_classes = [IsAuthenticated]
   
    # get method to get employee
    
    def get(self,request,id):
        try:
            employee = Employee.objects.get(id=id)
            employee_serializer = EmployeeSerializer(employee)
        except Exception as e:
            return Response({'Employee id {}'.format(e)},status=status.HTTP_404_NOT_FOUND)
        return Response(employee_serializer.data,status=status.HTTP_200_OK) 
   
    # put method to modify perticular empolyee
   
    def put(self,request,id):
        try:
            employee = Employee.objects.get(id=id)
            employee_serializer = EmployeeSerializer(employee,data=request.data)
            employee_serializer.is_valid(raise_exception=True)
            employee_serializer.save()
        except Exception as e:
            return Response({'message':'Employee not updated {}'.format(e)},status=status.HTTP_404_NOT_FOUND)
        return Response(employee_serializer.data,status=status.HTTP_200_OK)
    
    #delete employee detail
    
    def delete(self,request,id):
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
        except Exception as e:
             return Response({'Employee not deleted {}'.format(e)},status=status.HTTP_404_NOT_FOUND)
        return Response({'message':'Employee Deleted'}) 
                   


    
        
        
            
        
        
    
  # def post(self,request) :
    #     payload = json.dumps(request.data)
    #     payload = json.loads(payload)
    #     manager = request.manager
    #     employee = Employee.objects.create(email=payload['email'],firstname=payload['firstname'],lastname=payload['lastname'], address =payload['address'], date_of_birth= payload['date_of_birth'],city=payload['city'], phonenumber=payload['phonenumber'], manager=manager,)                                   
    #     employee_serializer = EmployeeSerializer(employee)
    #     status_code = status.HTTP_200_OK
    #     return Response(employee_serializer,status_code)    