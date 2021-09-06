from core.forms import ContatoForm
from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def contato(request):
    forms = ContatoForm(request.POST or None)
    context = {
        'forms':forms
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')

