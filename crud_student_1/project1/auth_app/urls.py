from django.urls import path
from . import views

urlpatterns=[
    path('sup/', views.signup_view, name='signup'),
    path('sin/', views.signin_view, name='signin'),
    path('log/', views.logout_view, name='logout'),

]