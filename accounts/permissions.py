from rest_framework import permissions
from .models import *


class IsAdmin(permissions.BasePermission):

    def __init__(self, allowed_methods):
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(Profiles.objects.all().filter(id=request.user.id)[
                        0].role == Profiles.ADMIN and request.method in self.allowed_methods)


class IsEmployee(permissions.BasePermission):

    def __init__(self, allowed_methods):
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(Profiles.objects.all().filter(id=request.user.id)[
                        0].role == Profiles.EMPLOYEE and request.method in self.allowed_methods)


class IsStudent(permissions.BasePermission):

    def __init__(self, allowed_methods):
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(Profiles.objects.all().filter(id=request.user.id)[
                        0].role == Profiles.STUDENT and request.method in self.allowed_methods)


class IsTeacher(permissions.BasePermission):

    def __init__(self, allowed_methods):
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(Profiles.objects.all().filter(id=request.user.id)[
                        0].role == Profiles.TEACHER and request.method in self.allowed_methods)
