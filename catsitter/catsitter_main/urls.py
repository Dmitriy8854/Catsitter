# ice_cream/urls.py
from django.urls import path
from . import views


app_name = 'catsitter_main'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком сортов мороженого
    #path('catsitter/', views.catsitter_list, name='catsitter_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # Отдельная страница с информацией о сорте мороженого
    path('catsitter/<int:post_id>/', views.catsitter_detail, name='catsitter_detail'),
    path('create/', views.post_create, name='post_create'),
    path('catsitter/<int:post_id>/edit/', views.post_edit, name='post_edit'),
] 