from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RecordViewSet

router = DefaultRouter()
router.register(r'records', RecordViewSet)

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-record/', views.create_record, name='create-record'),
    path('update-record/<int:pk>/', views.update_record, name='update-record'),
    path('delete-record/<int:pk>/', views.delete_record, name='delete-record'),
    path('record/<int:pk>/', views.view_record, name='record'),
    path('api/', include(router.urls)),
]
