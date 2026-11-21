from rest_framework import serializers
from .models import (Category, UserProfile, Course, CartItem, Cart, Teacher, Student, Question, CourseReview, Assignment, Links, Lesson, Exam, Answers, Certificate)

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'profile_picture', 'role')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name',)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('category', 'course_name', 'description', 'level', 'price', 'created_by', 'created_at', 'updated_at',)

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('cart', 'course', 'quantity',)

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'created_date',)

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('experience', 'teacher_role', 'bio')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_role',)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('exam', 'name_question', 'text',)

class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = ('user', 'course', 'rating', 'comment',)

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('name_assignment', 'description', 'due_date', 'course', 'student',)

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ('student','links_url',)

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('name_exam','course', 'passing_score', 'duration',)

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('lesson_name','video_url', 'content', 'course',)

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('questions','answers', 'true_answers',)

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('student','course', 'issued_at', 'certificate_url')



