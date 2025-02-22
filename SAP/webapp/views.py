from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona, Domicilio


# Create your views here.
def bienvenido(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.order_by('id')
    domicilios = Domicilio.objects.order_by('-id')
    return render(request, 'bienvenido.html',
                  {'no_personas':no_personas,
                   'personas':personas,
                   'domicilios':domicilios})

