from django.contrib.admin import ModelAdmin

from core.models import Produto
from django.contrib import admin

# Register your models here.
class ProdutoAdmin(ModelAdmin):
    model = Produto
    list_display = ['nome', 'slug']

admin.site.register(Produto, ProdutoAdmin)