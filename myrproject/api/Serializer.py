from rest_framework import serializers
from student.models import Stundent
from employees.models import Employee

class StudentSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Stundent
        fields='__all__'


#serializer for the employee

class EmpolyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
        
       