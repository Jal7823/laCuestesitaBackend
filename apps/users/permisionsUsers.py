from rest_framework.permissions import BasePermission

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            return False  # Denegar acceso si el usuario no está autenticado
        
        # Verificar si el usuario es staff
        return request.user.is_staff

class IsEmploye(BasePermission):
    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            return False  # Denegar acceso si el usuario no está autenticado
        
        # Verificar si el usuario tiene el rol de 'employe'
        return request.user.role == 'employe'

class IsBoss(BasePermission):
    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            return False  # Denegar acceso si el usuario no está autenticado
        
        # Verificar si el usuario tiene el rol de 'boss'
        return request.user.role == 'boos'
