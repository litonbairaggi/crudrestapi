from django.urls import path
from crudapi import views 

urlpatterns = [
    path('teacherinfo', views.TeacherDetailListView.as_view()),
    path('teacherinfo/<int:pk>', views.TeacherDetailView.as_view()),
    path('qualification', views.QualificationListView.as_view()),
    path('qualification/<int:pk>', views.QualificationView.as_view()),
]