from django.http import HttpResponse


def index(request):
    return HttpResponse('Юху! У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
