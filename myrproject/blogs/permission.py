from rest_framework.permissions import BasePermission

class BlogPermission(BasePermission):
    def has_permission(self, request, view):  #genreal allow 
        # anyone can read
        if request.method=='GET':
            return True
         # must be logged in
        if not request.user.is_authenticated:
            return False
        # superadmin full access
        if request.user.is_superuser:
            return True
        # author → allow create + update + delete
        if request.user.profile.role=='author':
            return request.method in['POST','PUT', 'PATCH', 'DELETE']
        return False
    def has_object_permission(self, request, view, obj):  #chekck the owenership 
          # superadmin → full access
        if request.user.is_superuser:
            return True
        # author → only own blog
        if request.user.profile.role=='author':
            return obj.user==request.user
         # reader → only read
        return request.method=='GET'
    