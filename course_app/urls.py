from rest_framework import routers
from .views import (UserProfileViewSet, CategoryViewSet, CourseViewSet, CartItemViewSet, CartViewSet, TeacherViewSet, StudentViewSet, QuestionViewSet, CourseReviewViewSet,
                   AssignmentViewSet, LinksViewSet, ExamViewSet, LessonViewSet, AnswersViewSet, CertificateViewSet)
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'Users', UserProfileViewSet)
router.register(r'Category', CategoryViewSet)
router.register(r'Course', CourseViewSet)
router.register(r'CartItem', CartItemViewSet)
router.register(r'Cart', CartViewSet)
router.register(r'Teacher', TeacherViewSet)
router.register(r'Student', StudentViewSet)
router.register(r'Question', QuestionViewSet)
router.register(r'CourseReview', CourseReviewViewSet)
router.register(r'Assignment', AssignmentViewSet)
router.register(r'Links', LinksViewSet)
router.register(r'Exam', ExamViewSet)
router.register(r'Lesson', LessonViewSet)
router.register(r'Answers', AnswersViewSet)
router.register(r'Certificate', CertificateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]