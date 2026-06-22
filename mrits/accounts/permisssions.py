from rest_framework.permissions import BasePermission

class IsFaculty(BasePermission):
    def has_permission(self, request, view):
        return request.user.role=='faculty'

class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return request.user.role == 'admin'
    
class IsStudent(BasePermission):
    def has_permission(self,request,view):
        return request.user.role == 'student'