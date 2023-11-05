from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'SethubApp/index.html', context=data)


def create(request):
    data = {
        'title': 'Создание сета',
    }
    return render(request, 'SethubApp/create.html', context=data)