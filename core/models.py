from django.db import models

from services.doc_processor import read_file_txt


class Arquivo(models.Model):
    arquivo = models.FileField("Upload do arquivo", upload_to="")
    dt_criado = models.DateTimeField("Data de Cadastro", auto_now_add=True)

    def __str__(self):
        return str(self.arquivo)

    def save(self, *args, **kwargs):
        super(Arquivo, self).save(*args, **kwargs)
        arquivo_vendas = read_file_txt(self.arquivo.path)
        lote = Lote.objects.create(
            arquivo=self, total_lote=arquivo_vendas["total_vendas"]
        )
        result_list = []
        for transacao in arquivo_vendas["vendas"]:
            transacao["lote"] = lote
            result_list.append(Venda(**transacao))
        Venda.objects.bulk_create(result_list)

    class Meta:
        verbose_name_plural = "Importar Arquivo"


class Lote(models.Model):
    dt_criado = models.DateTimeField("Data de Cadastro", auto_now_add=True)
    arquivo = models.ForeignKey(
        Arquivo,
        related_name="lote_arquivo",
        verbose_name="Arquivo",
        on_delete=models.DO_NOTHING,
    )
    total_lote = models.DecimalField(
        "Total da Venda", decimal_places=2, max_digits=10, default=0
    )

    def __str__(self):
        return f"Lote {self.arquivo.id} - {self.arquivo}"


class Venda(models.Model):
    comprador = models.CharField("Comprador", max_length=30)
    descricao = models.TextField("Descrição", max_length=150)
    preco_und = models.DecimalField(
        "Preço Unitário", decimal_places=2, max_digits=6, default=0
    )
    quantidade = models.PositiveIntegerField("Quantidade", default=0)
    endereco = models.TextField("Endereço", max_length=150)
    fornecedor = models.CharField("Fornecedor", max_length=30)
    total_venda = models.DecimalField(
        "Total da Venda", decimal_places=2, max_digits=6, default=0
    )
    lote = models.ForeignKey(
        Lote,
        related_name="venda_lote",
        on_delete=models.DO_NOTHING,
        verbose_name="Lote",
    )

    def __str__(self):
        return self.comprador

    class Meta:
        verbose_name = "Venda"
