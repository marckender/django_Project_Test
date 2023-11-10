from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("noticia/<int:id>/", views.detalhes, name="noticia")
]