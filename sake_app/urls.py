from django.urls import path
from . import views

urlpatterns = [
    path('', views.sake_list, name='sake_list'),  # 客戶展示頁面
    path('manage/', views.sake_management, name='sake_management'),  # 管理頁面
    path('create/', views.sake_create, name='sake_create'),
    path('update/<int:pk>/', views.sake_update, name='sake_update'),
    path('delete/<int:pk>/', views.sake_delete, name='sake_delete'),
]