from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
  return HttpResponse('Hola Django - Coder')
