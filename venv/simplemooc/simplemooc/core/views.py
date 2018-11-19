from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    #render(METODO, TEMPLATE, CONTEXTO)
    return render(request, 'home.html', {'usuario':'Bruno Silva'})
    #return HttpResponse('Alo Mundo!')
