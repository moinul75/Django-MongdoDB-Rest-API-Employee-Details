from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import DepertmentSerializer,EmployeeSerializer
from .models import Depertment,Employee
from django.core.files.storage import default_storage





# Create your views here.
@csrf_exempt
def DepartmentAPI(request,id=0):
    #get method 
    if request.method == 'GET':
        dept_data = Depertment.objects.all()
        department_serializer = DepertmentSerializer(dept_data,many = True)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        department_serializer = DepertmentSerializer(data=data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse(department_serializer.errors,safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        depratment = Depertment.objects.get(DepertmentId=data['DepertmentId'])
        department_serializer = DepertmentSerializer(depratment,data=data)
        if department_serializer.is_valid():
            return JsonResponse("Successfully Updated",safe=False)
        return JsonResponse("Something is went wrong...ops",safe=False)
    elif request.method == 'DELETE':
        department = Depertment.objects.get(DepertmentId=id)
        department.delete()
        return JsonResponse("Successfully Deleted..",safe=False)
    
    
#Employee CRUD 
@csrf_exempt
def EmployeeAPI(request,id=0):
    if request.method == 'GET':
        employee_data = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee_data,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Successfully Added AN Employee",safe=False)
        return JsonResponse(employee_serializer.errors,safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            return JsonResponse("Successfully Updated",safe=False)
        return JsonResponse("Failed to Updatad.. ",safe=False)
    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Successfully Deleted..",safe=False)
    
#Files uploaded API 
@csrf_exempt
def FIleAPI(request):
    file = request.FILES['file']
    file_save = default_storage.save(file.name,file)
    return JsonResponse(file_save,safe=False)
    
    
        
  