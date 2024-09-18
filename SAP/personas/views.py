from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio


# Create your views here.
def detallePersona(request, id):
    # try:
    #     persona = Persona.objects.get(pk=id)
    # except Persona.DoesNotExist:
    #     raise Http404("Persona no encontrada")
    persona = get_object_or_404(Persona, id = id)
    return render(request, 'personas/detalle.html', {'persona':persona})

# PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request, domicilio_id=None):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()

        if domicilio_id:
            domicilio = get_object_or_404(Domicilio, id=domicilio_id)
            formaPersona.fields['domicilio'].initial = domicilio
    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})

def nuevoDomicilioPersona(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            nuevo_domicilio = formaDomicilio.save()
            return redirect('nueva_persona', domicilio_id=nuevo_domicilio.id)
    else:
        formaDomicilio = DomicilioForm()
    return render(request, 'domicilios/nuevo.html', {'formaDomicilio':formaDomicilio})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona) # Django necesita que se diga la instancia q se modificara
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona':formaPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if persona:
        persona.delete()
    return redirect('index')

#### Creando Apartado Domicilios
def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm()
    return render(request, 'domicilios/nuevo.html', {'formaDomicilio':formaDomicilio})

def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, id = id)
    return render(request, 'domicilios/detalle.html', {'domicilio':domicilio})

def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, id=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio) # Django necesita que se diga la instancia q se modificara
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)
    return render(request, 'domicilios/editar.html', {'formaDomicilio':formaDomicilio})

def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, id=id)
    if domicilio:
        domicilio.delete()
    return redirect('index')