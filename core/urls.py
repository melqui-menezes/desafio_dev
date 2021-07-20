from django.urls import path
from .views import LoteView, ArquivoView, VendaView

urlpatterns = [
    path("",ArquivoView.as_view(), name="index"),
    path("lotes", LoteView.as_view(), name="lotes"),
    path("lotes/<int:lote_pk>/transacoes",VendaView.as_view(), name="transacoes"),
    ]