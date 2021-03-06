# Generated by Django 3.2.5 on 2021-07-18 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Arquivo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "arquivo",
                    models.FileField(
                        upload_to="docs", verbose_name="Upload do arquivo"
                    ),
                ),
                (
                    "dt_criado",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Cadastro"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Importar Arquivo",
            },
        ),
        migrations.CreateModel(
            name="Lote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dt_criado",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Cadastro"
                    ),
                ),
                (
                    "total_lote",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="Total da Venda",
                    ),
                ),
                (
                    "arquivo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="lote_arquivo",
                        to="core.arquivo",
                        verbose_name="Arquivo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Venda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "comprador",
                    models.CharField(max_length=30, verbose_name="Comprador"),
                ),
                (
                    "descricao",
                    models.TextField(max_length=150, verbose_name="Descri????o"),
                ),
                (
                    "preco_und",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=6,
                        verbose_name="Pre??o Unit??rio",
                    ),
                ),
                (
                    "quantidade",
                    models.PositiveIntegerField(default=0, verbose_name="Quantidade"),
                ),
                ("endereco", models.TextField(max_length=150, verbose_name="Endere??o")),
                (
                    "fornecedor",
                    models.CharField(max_length=30, verbose_name="Fornecedor"),
                ),
                (
                    "total_venda",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=6,
                        verbose_name="Total da Venda",
                    ),
                ),
                (
                    "lote",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="venda_lote",
                        to="core.lote",
                        verbose_name="Lote",
                    ),
                ),
            ],
            options={
                "verbose_name": "Venda",
            },
        ),
    ]
