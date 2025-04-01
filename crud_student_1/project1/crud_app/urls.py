from django.urls import path
from . import views

urlpatterns=[
    path('student/', views.student_create_view, name='student'),
    path('retrive/', views.student_retirve_view, name='retrive'),
    path('update/<pk>/', views.student_update_view, name='update'),
    path('delete/<pk>/', views.student_delete_view, name='delete'),
]