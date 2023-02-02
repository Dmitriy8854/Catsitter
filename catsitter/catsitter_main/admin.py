from django.contrib import admin

# Из модуля models импортируем модель Post
from .models import Questionnaire

class QuestionnaireAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('name', 'description', 'location', 'price', 'pub_date', 'author') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',) 

admin.site.register(Questionnaire, QuestionnaireAdmin) 
