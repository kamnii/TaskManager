from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_api_view),
    path('<int:pk>/', views.task_detail_api_view),
    path('tags/', views.tag_list_api_view)
]