from django.contrib import admin

from .models import Arquivo, Lote, Venda


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ["arquivo", "dt_criado"]


@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ["id", "arquivo", "dt_criado", "total_lote"]


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = [
        "lote",
        "comprador",
        "descricao",
        "preco_und",
        "quantidade",
        "endereco",
        "fornecedor",
        "total_venda",
    ]
    exclude = [
        "comprador",
        "descricao",
        "preco_und",
        "quantidade",
        "endereco",
        "fornecedor",
        "total_venda",
    ]
