# coding: utf8
from django.contrib import admin

# Register your models here.
from .models import School, Grade, Class, Exam


class GradeInline(admin.StackedInline):
    model = Grade
    extra = 0

class ClassInline(admin.StackedInline):
    model = Class
    extra = 0

class SchoolAdmin(admin.ModelAdmin):
    search_fields = ['name']
    fieldsets = [
        (None, {'fields':['name']}),
    ]

class GradeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    fieldsets = [
        (None, {'fields': ['name']}),
    ]

class ClassAdmin(admin.ModelAdmin):
    list_display = ['school', 'grade', 'name']
    fieldsets = [
        (None, {'fields':['school', 'grade']}),
        (None, {'fields': ['name']}),
    ]

class ExamAdmin(admin.ModelAdmin):
    list_display = ['school', 'grade', 'name']
    fieldsets = [
        (None, {'fields': ['school', 'grade']}),
        (None, {'fields': ['name']}),
    ]

admin.site.register(School, SchoolAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Exam, ExamAdmin)
