from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from .models import *

#pk=view.kwargs['id']


class CoursePermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST','PUT','DELETE']:
                masterAccount = Institute.objects.filter(user__username=request.user.username).count()>0
                admin=ProfileRole.objects.filter(user__user__username=request.user.username,role='admin').count()>0
                if admin or masterAccount:
                    return True
                else:
                    return False
            if request.method == 'GET':
                masterAccount = Institute.objects.filter(user__username=request.user.username).count()>0
                confirm=Profile.objects.filter(user__username=request.user.username).count()>0
                if confirm or masterAccount:
                    return True
        return False


def CourseQuerySet(request):
    if Institute.objects.filter(user__username=request.user.username).count()>0:
        return Course.objects.filter(institute__user__username=request.user.username)
    corp = Profile.objects.get(user__username=request.user.username).corp.user.username
    return Course.objects.filter(institute__user__username=corp)


class LessonPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST','PUT','DELETE']:
                admin=Institute.objects.filter(user__username=request.user.username).count()>0
                groupadmin=ProfileRole.objects.filter(user__user__username=request.user.username , ROLE_CHOICES='groupadmin').count()>0
                if admin  or groupadmin:
                    return True
                else:
                    return False
            if request.method == 'GET':
                confirm=Profile.objects.filter(user__username=request.user.username).count()>0
                return confirm
        return True

def LessonQuerySet(request):
    if Institute.objects.filter(user__username=request.user.username).count()>0:
        return Lesson.objects.filter(institute__user__username=request.user.username)
    corp = Profile.objects.get(user__username=request.user.username).corp.user.username
    return Lesson.objects.filter(course__institute=corp)

class LessonQuestionPermission(BasePermission):
    message='You are not authorized to this data'
    SAFE_METHOD = ['GET','POST','PUT','DELETE']
    def has_permission(self, request, view):
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST','PUT','DELETE']:
                admin=Institute.objects.filter(user__username=request.user.username).count()>0
                groupadmin=ProfileRole.objects.filter(user__user__username=request.user.username , ROLE_CHOICES='groupadmin').count()>0
                if admin  or groupadmin:
                    return True
                else:
                    return False
            if request.method == 'GET':
                confirm=Profile.objects.filter(user__username=request.user.username).count()>0
                return confirm
        return True

   
def LessonQuestionQuerySet(request):
    corp = Profile.objects.get(user__username=request.user.username).corp
    return LessonQuestion.objects.filter(lession_course__institute=corp)

    if Institute.objects.filter(user__username=request.user.username).count()>0:
        return Lesson.objects.filter(institute__user__username=request.user.username)
    corp = Profile.objects.get(user__username=request.user.username).corp.user.username
    return Lesson.objects.filter(course__institute=corp)





