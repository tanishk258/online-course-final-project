from django.contrib import admin
from .models import Question, Choice, Submission, Course, Lesson, Enrollment, User

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionInline(admin.TabularInline):
    model = Question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
