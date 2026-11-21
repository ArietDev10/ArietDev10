from django.contrib import admin
from .models import (Category, UserProfile, Course, CartItem, Cart, Teacher, Student, Question, CourseReview, Assignment, Links, Lesson, Exam, Answers, Certificate)

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Certificate)
admin.site.register(CourseReview)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Lesson)
admin.site.register(Links)
admin.site.register(Exam)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Answers)
admin.site.register(Assignment)

