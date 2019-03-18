from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'blog'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('edit/<int:article_id>/', views.edit_page, name='edit_page'),
    path('edit/action/', views.edit_action, name='edit_action'),
    path('article/<int:article_id>/', views.article_page, name='article_page'),
]