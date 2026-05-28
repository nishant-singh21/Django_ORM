from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/', views.post_profile, name='post_profile'),
]