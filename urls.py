from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('create/', views.create_movie, name='create_movie'),
]