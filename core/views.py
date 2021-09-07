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
            forms.send_mail()

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

