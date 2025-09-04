from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allows users to edit only thier own profile"""
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
   
    
class UpdateOwnStatus(permissions.BasePermission):
    """ Allows users to update only their status"""
    
    def has_object_permission(self, request, view, obj):
       
       if request.method in permissions.SAFE_METHODS:
           return True
       
       return obj.user_profile.id == request.user.id