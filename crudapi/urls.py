from django.urls import path
from crudapi import views 

urlpatterns = [    
    path('teacherinfo/get', views.get_teacherinfo),
    path('teacherinfo/get/<int:pk>', views.get_teacherinfo_detail),
    path('teacherinfo/post', views.post_teacherinfo),
    path('teacherinfo/post/<int:pk>', views.post_teacherinfo_detail),
    path('teacherinfo/put/<int:pk>', views.update_teacherinfo),
    path('teacherinfo/delete/<int:pk>', views.delete_teacherinfo),

    path('quali/get', views.get_qualification),
    path('quali/get/<int:pk>', views.get_qualification_detail),
    path('quali/post', views.post_qualification),
    path('quali/post/<int:pk>', views.post_qualification_detail),
    path('quali/put/<int:pk>', views.update_qualification),
    path('quali/delete/<int:pk>', views.delete_qualification),
]