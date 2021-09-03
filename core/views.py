from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def contato(request):
    return render(request, 'contato.html')

def produto(request):
    return render(request, 'produto.html')

