from rest_framework import serializers

from employees.models import Employee




#serializer for the employee

class EmpolyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
        
       