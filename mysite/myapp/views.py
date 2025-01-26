from django.shortcuts import render

# Create your views here.
# mysite/myapp/views.py
from django.http import HttpResponse, HttpRequest


# Поздравляю, это ваш первый контроллер, который может принять запрос и отдать ответ с текстом, больше ничего
def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hey! It's your main view!!")

def another(request: HttpRequest) -> HttpResponse:
    return HttpResponse("It's another page!!")

def main_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse('There will be a list with articles')


def uniq_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is a unique answer for a unique value')


def article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"This is article #{article_id}.")