from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('client', 'client'),
    ('teacher', 'teacher'),
    ('administrator', 'administrator'),
)

LEVEL_CHOICES = (
    ('beginner', 'beginner '),
    ('intermediate', 'intermediate'),
    ('advanced', 'advanced'),
)

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

class Teacher(UserProfile):
    experience = models.PositiveSmallIntegerField(default=0)
    teacher_role = models.CharField(max_length=20, choices=(('teacher', 'teacher'),), default='teacher')
    bio = models.TextField(blank=True)

class Student(UserProfile):
    student_role = models.CharField(max_length=20, choices=(('client', 'client'),), default='client')

class Links(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    links_url = models.URLField()

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    level = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=50)
    video_url = models.FileField(upload_to='lesson_videos/', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Assignment(models.Model):
    name_assignment = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Exam(models.Model):
    name_exam = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField(default=0)
    duration = models.PositiveSmallIntegerField(default=0)

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name_question = models.CharField(max_length=50, unique=True)
    text = models.TextField(null=True, blank=True)

class Answers(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.TextField(null=True, blank=True)
    true_answers = models.TextField(null=True, blank=True)

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.URLField()

class CourseReview(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=4)
    comment = models.TextField(null=True, blank=True)

class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.cart.items.all())





























