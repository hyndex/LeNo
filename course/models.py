from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from django.db.models import Q
from users.models import *
from media.models import *
from quiz.models import *


class Course(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    category = models.CharField(max_length=50, blank=False, null=True, default = '')
    media = models.ForeignKey(Media, on_delete=models.PROTECT,blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    instructor = models.ForeignKey(Profile,on_delete=models.PROTECT)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField(blank=False, null=True, default = 0)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.TextField(blank=False, null=True, default = '')
    media = models.ForeignKey(Media, on_delete=models.PROTECT,blank=True, null=True)
    question_number = models.IntegerField(blank=True, null=True,default=0)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)

class LessonQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

class GroupAllocation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT,blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT,blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)


    
