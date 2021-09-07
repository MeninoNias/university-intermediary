from core.forms import ContatoForm
from django.shortcuts import render
from django.contrib import messages

def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def contato(request):
    forms = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if forms.is_valid():
            nome = forms.cleaned_data['nome']
            email = forms.cleaned_data['email']
            assunto = forms.cleaned_data['assunto']
            menssagem = forms.cleaned_data['menssagem']

            print('Menssagem enviada')
            print('nome', nome)
            print('email', email)
            print('assunto', assunto)
            print('menssagem', menssagem)

            messages.success(request, "E-mail enviado com sucesso")
            forms = ContatoForm()
        else:
            messages.error(request, "Erro ao enviar e-mail")

    context = {
        'forms':forms
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')

