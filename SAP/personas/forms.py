from django.forms import ModelForm, EmailInput, TextInput

from personas.models import Persona, Domicilio


class PersonaForm(ModelForm):
    class Meta:
        model = Persona # Clase de tipo modelo que usara
        fields = '__all__' # Que campos se usaran (nombre, apellido, email, etc.)
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio # Clase de tipo modelo que usara
        fields = '__all__' # Que campos se usaran (nombre, apellido, email, etc.)
        widgets = {
            'no_calle': TextInput(attrs={'type': 'number'})
        }