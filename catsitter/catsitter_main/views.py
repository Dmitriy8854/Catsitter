from django.shortcuts import render

# Create your views here.
# ice_cream/views.py
from django.http import HttpResponse


# Главная страница

def index(request):
    template = 'catsitter_main/index.html'
    return render(request, template)

#«Добавлены urls и view-функции»
# Страница со списком мороженого
def catsitter_list(request):
    template = 'catsitter_main/catsitter_list.html'
    return render(request, template)



# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def catsitter_detail(request, pk):
    return HttpResponse(f'Котоняня {pk}') 