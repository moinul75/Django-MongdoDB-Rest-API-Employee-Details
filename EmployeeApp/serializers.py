from rest_framework import serializers
from .models import Employee,Depertment


#Depertment serializers
class DepertmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depertment
        fields = ('DepertmentId','DepertmentName')
        


#employee Serializers 
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeId','EmployeeName','Depertment','DataOfJoining','photoFileName')