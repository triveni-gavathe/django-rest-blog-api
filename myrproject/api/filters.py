import django_filters
from employees.models import Employee
from blogs.models import Blog
class EmployeeFilter(django_filters.FilterSet):
    emp_name=django_filters.CharFilter(
        field_name='emp_name',
        lookup_expr='icontains'   #its is used for the all similar words 
    )
    designation=django_filters.CharFilter(
        field_name='designation',
        lookup_expr='iexact'  #ITS IS CAN accpet the uper case lower case show the result
    )
    class Meta:
        model=Employee
        fields=['emp_name','designation']
        
    
class BlogFilter(django_filters.FilterSet):
    blog_title=django_filters.CharFilter(field_name='blog_title',
                                         lookup_expr='icontains')
    class Meta:
        model=Blog    
        fields=['blog_title']
