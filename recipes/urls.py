from django.urls import path
from recipes.views import Home, Contato, Sobre
urlpatterns = [
    path('sobre/', Sobre),
    path('contato/',Contato),
    path('',Home)
]