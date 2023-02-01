# ice_cream/urls.py
from django.urls import path
from . import views




urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком сортов мороженого
    path('catsitter/', views.catsitter_list),
    # Отдельная страница с информацией о сорте мороженого
    path('catsitter/<int:pk>/', views.catsitter_detail),
] 