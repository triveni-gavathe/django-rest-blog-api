from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from student.models import Stundent
from api.Serializer import StudentSerializer

# Create your views here.

def students(request):
    stundents=[{
        'id':1,
        'name':'triveni',
        'age':21
    }
    ]
    return HttpResponse(stundents)


@api_view(['GET','POST'])
def studentView(request):
    # students=Stundent.objects.all()
    # print(students)
    # #serizlaie the dta manually
    # #covert into the list 
    # student_lst=list(students.values())
    if request.method=='GET':
        students=Stundent.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=='POST':
        print("request body :",request.data)
        serializer=StudentSerializer(data=request.data)
        #get the data
        print("before serilizer:",serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print("after",serializer)  
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
# GEtting the data frm the id using the primary key
def studentdetailview(request,pk):
    try:
        studet_q=Stundent.objects.get(pk=pk)
    except Stundent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
    if request.method=='GET':
        serializer=StudentSerializer(studet_q)  
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=StudentSerializer(studet_q,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        studet_q.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)