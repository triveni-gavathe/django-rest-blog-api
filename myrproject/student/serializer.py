from rest_framework import serializers
from student.models import Stundent
class StudentSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Stundent
        fields='__all__'