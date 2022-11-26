from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Отображение главной страницы"""
    name = request.GET.get(key='name')
    message = request.GET.get(key='message')
    example = None
    if name is None or message is None:
        name = "Передайте параметр: name"
        message = 'и параметр: message'
        example = '?name=Rekruto&message=Давай%20дружить!'

    context = {
        'name': name,
        'message': message,
        'example': example
    }
    return render(request, 'index.html', context=context)
