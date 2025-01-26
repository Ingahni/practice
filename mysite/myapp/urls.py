from django.urls import path
from .views import main_article, uniq_article, article

urlpatterns = [
    path('', main_article, name='main_article'),
    path('33/', uniq_article, name='unique_article'),
    path('<int:article_id>/', article, name='article'),
    path('<int:article_id>/<slug:name>', article, name='article_name'),
]