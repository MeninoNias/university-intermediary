from core.forms import ContatoForm, ProdutoForm
from django.shortcuts import render
from django.contrib import messages

from core.models import Produto


def index(request):
    template_name = 'index.html'
    produtos = Produto.objects.all()
    context = {
        "produtos":produtos
    }
    return render(request, template_name, context)

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
    if str(request.method) == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto salvo com sucesso")
            form = ProdutoForm()
        else:
            messages.error(request, "Erro ao salvar produto")
    else:
        form = ProdutoForm()
    context = {
        'forms': form
    }
    return render(request, 'produto.html', context)

