from django.urls import path

from .views import index, contato, produto

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto', produto, name='produto')
]
