from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render
from .models import Noticia


def index(request):
  noticias = Noticia.objects.all()
  return render(request, 'index.html', {'noticias': noticias})

def detalhes(request, id):
  noticia = Noticia.objects.get(pk=id)
  return render(request,
                'detalhes.html',
                {'noticia': noticia})
