from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.ReisterView.as_view()),
    path('login/', views.LoginView.as_view()),
]