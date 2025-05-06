from django.urls import path
from sistema import views


# Informa qual será a rota que irá chamar determinada viwe(função)
urlpatterns = [
    path('', views.index),
    path('apresentacao/', views.apresentacao),
    path('listar/', views.listarUsuarios),
    path('filmes/', views.listarFilmes),
]
