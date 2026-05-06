from django.urls import path
from .views import studentView, studentdetailview

urlpatterns = [
    path('', studentView),
    path('<int:pk>/', studentdetailview),
]