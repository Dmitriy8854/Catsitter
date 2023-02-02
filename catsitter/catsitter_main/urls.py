# ice_cream/urls.py
from django.urls import path
from . import views


app_name = 'catsitter_main'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком сортов мороженого
    path('catsitter/', views.catsitter_list, name='catsitter_list'),
    # Отдельная страница с информацией о сорте мороженого
    path('catsitter/<int:pk>/', views.catsitter_detail, name='catsitter_list'),
] 