from rest_framework import permissions
from .models import *


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(Profile.objects.all().filter(id=request.user.id)[
                        0].role == Profile.ADMIN)


class IsEmployee(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(Profile.objects.all().filter(id=request.user.id)[
                        0].role == Profile.EMPLOYEE)


class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(Profile.objects.all().filter(id=request.user.id)[
                        0].role == Profile.STUDENT)


class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(Profile.objects.all().filter(id=request.user.id)[
                        0].role == Profile.TEACHER)
