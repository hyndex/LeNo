from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .permissions import *
import datetime as dt

class lessonCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields='__all__'
        read_only_fields=('date_updated',)

class CourseSerializer(serializers.ModelSerializer):
    lessons=lessonCourseSerializer(many=True,read_only=True,source='lessonCourse')
    class Meta:
        model = Course
        fields=('id','institute','name','description','category','media','original','media360','media720','thumbnail','instructor','lessons','date_updated')
        read_only_fields=('date_updated','institute','lessons','instructor','original','media360','media720')

    def create(self, validated_data):
        username = self.context['request'].user.username
        if Institute.objects.filter(user__username=username).count()>0:
            corp = self.context['request'].user.username
        else:
            corp = Profile.objects.get(user__username=username).corp.user.username
        institute=Institute.objects.get(user__username=corp)
        instructor=Profile.objects.filter(user__username=username)
        if instructor.count()>0:
            instructor=instructor[0]
        else:
            instructor=None
        course = Course.objects.create(institute=institute,instructor=instructor,**validated_data)
        return course

    def update(self, instance, validated_data):
        
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.category=validated_data.get('category',instance.category)
        instance.media=validated_data.get('media',instance.media)
        instance.thumbnail=validated_data.get('thumbnail',instance.thumbnail)
        # instance.instructor=validated_data.get('instructor',instance.instructor)
        instance.date_updated=dt.datetime.now()
        instance.save()
        return instance

class LessonSerializer(serializers.ModelSerializer):
    course = serializers.CharField(write_only=True)
    class Meta:
        model = Lesson
        fields=('id','course','number','name','description','media','original','media360','media720','thumbnail','date_updated')
        read_only_fields=('date_updated','media','original','media360','media720','thumbnail')
        depth = 1

    def create(self, validated_data):
        course_id = validated_data.pop('course')
        course=Course.objects.get(id=course_id)
        lession = Lesson.objects.create(course=course,**validated_data)
        return lession

    def update(self, instance, validated_data):
        course_id = validated_data.pop('course')
        course=Course.objects.get(id=course_id)

        instance.number=validated_data.get('number',instance.number)
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.media=validated_data.get('media',instance.media)
        instance.question_number=validated_data.get('question_number',instance.question_number)
        instance.date_updated=dt.datetime.now()
        instance.save()
        return instance




