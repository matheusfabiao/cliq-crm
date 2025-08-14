from django.urls import path

from . import views

urlpatterns = [
    path('', views.ai_chat, name='ai_chat'),
    path('response/', views.response, name='response'),
]
