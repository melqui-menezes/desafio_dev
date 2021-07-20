from django.forms import models
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy

from .models import Venda, Arquivo, Lote


class ArquivoView(CreateView):
    models = Arquivo
    template_name = "import_arquivo.html"
    queryset = Arquivo.objects.all()
    fields = ["arquivo",]
    success_url = reverse_lazy("lotes")


class VendaView(ListView):
    models = Venda
    template_name = "transacoes.html"
    queryset = Venda.objects.all()
    context_object_name = "transacoes"
    
    def get_queryset(self):
        if self.kwargs.get('lote_pk'):
            return self.queryset.filter(lote_id=self.kwargs.get('lote_pk'))
        return self.queryset.all()

class LoteView(ListView):
    models = Lote
    template_name = "lotes.html"
    queryset = Lote.objects.all()
    context_object_name = "lotes"
    
