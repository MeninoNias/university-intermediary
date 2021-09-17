from typing import Mapping
from django import forms
from django.forms.widgets import Textarea
from django.core.mail.message import EmailMessage

from .models import Produto

class ContatoForm(forms.Form):
    nome  = forms.CharField(label="Nome")
    email  = forms.EmailField(label="Email")
    assunto  = forms.CharField(label="Assunto")
    menssagem  = forms.CharField(label="Menssagem", widget=Textarea())


    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        menssagem = self.cleaned_data['menssagem']

        conteudo = f"Nome: {nome}\nAssunto: {assunto}\nMenssagem: {menssagem}"

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email="ananias.nobrega@gmail.com",
            to=["ananias.nobrega@gmail.com",],
            headers={"Replay-To": email}
        )
        mail.send()

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['name', 'preco', 'estoque', 'imagem']