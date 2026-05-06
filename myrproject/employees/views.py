from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from api.Serializer import EmpolyeeSerializer
from employees.serializer import EmployeeSerializer
from .models import Employee
from rest_framework import generics
from rest_framework import mixins
from api.paginations import custompagination,Mycursorpaginatation,Mylimitoffset
from api.filters import EmployeeFilter


# Create your views here.
class Employees(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmpolyeeSerializer
    pagination_class=custompagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class =EmployeeFilter
    search_fields=['emp_name','emp_id']
    ordering_fields=['emp_id','emp_name']
    permission_classes=[IsAuthenticated]
   
#generics
class EmployeesDetail(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
   queryset=Employee.objects.all()
   serializer_class=EmployeeSerializer
   lookup_field='pk'
    
    
# #class based view    
# class Employees(APIView): # its decide which is go to which part
#     def get(self,request):
#         employees=Employee.objects.all()
#         serializer=EmpolyeeSerializer(employees,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
        
#     def post(self,request):
#         serializer=EmpolyeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeesDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
#     def get(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmpolyeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)    
#     def put(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmpolyeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         Employee=self.get_object(pk)
#         Employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)           
            
# mixin concept
'''
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    queryset=Employee.objects.all()
    serializer_class=EmpolyeeSerializer
           
           
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class EmployeesDetail(generics.GenericAPIView,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmpolyeeSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
     
'''




#Generic view 


   
    

#viewset
'''
class EmployeeViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Employee.objects.all()
        serializer=EmpolyeeSerializer(queryset,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer=EmpolyeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def retrieve(self,request,pk=None):
        employee=get_object_or_404(Employee,pk=pk)
        serializer=EmpolyeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def update(self,request,pk=None):
        employee=get_object_or_404(Employee,pk=pk)
        serializer=EmpolyeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk=None):
        employee=get_object_or_404(Employee,PK=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
     
'''

#modelviewset
'''
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmpolyeeSerializer
'''
 