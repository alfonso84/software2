#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from groupthree.models import Juego, Sala

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request=request, *args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Pasword'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class SalaCreateForm(forms.ModelForm):
    juego = forms.ModelChoiceField(label=u'Juego', queryset=Juego.objects.all())
    capacidad_maxima = forms.IntegerField(label=u'Número de Jugadores')
    es_publica = forms.BooleanField(label='¿Es pública?', initial=False, required=False)
    pozo_por_jugador = forms.DecimalField(max_digits=5, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(SalaCreateForm, self).__init__(*args, **kwargs)
        self.fields['juego'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['capacidad_maxima'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['es_publica'].widget.attrs = {
            'class': 'checkbox'
        }
        self.fields['pozo_por_jugador'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Sala
        fields = [
            'juego',
            'capacidad_maxima',
            'es_publica',
             'pozo_por_jugador',
        ]
