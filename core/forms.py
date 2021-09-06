from django import forms
from django.forms.widgets import Textarea

class ContatoForm(forms.Form):
    nome  = forms.CharField(label="Nome")
    email  = forms.EmailField(label="Email")
    assunto  = forms.CharField(label="Assunto")
    messagem  = forms.CharField(label="Menssagem", widget=Textarea())
