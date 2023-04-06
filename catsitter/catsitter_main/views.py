from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Questionnaire
# Create your views here.
# ice_cream/views.py
from django.http import HttpResponse


# Главная страница

def index(request):
    template = 'catsitter_main/index.html'
    quest_list = Questionnaire.objects.all().order_by('-pub_date')
    paginator = Paginator(quest_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    questionnaires = Questionnaire.objects.order_by('-pub_date')[:10]
    context = {
        'questionnaires': questionnaires,
        'page_obj': page_obj,

    }
    return render(request, template, context)


#«Добавлены urls и view-функции»
# Страница со списком мороженого
def catsitter_list(request):
    template = 'catsitter_main/catsitter_list.html'
    return render(request, template)



# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def catsitter_detail(request, pk):
    return HttpResponse(f'Котоняня {pk}') 