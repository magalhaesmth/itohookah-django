# Generated by Django 4.1.5 on 2023-04-11 01:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0002_categoria_cliente_fabricante_funcionario_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produto",
            name="fabricante",
        ),
        migrations.RemoveField(
            model_name="produto",
            name="quantidade",
        ),
        migrations.AddField(
            model_name="categoria",
            name="atualizado_em",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="categoria",
            name="cadastrado_em",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fabricante",
            name="atualizado_em",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="fabricante",
            name="cadastrado_em",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="marca",
            name="atualizado_em",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="marca",
            name="cadastrado_em",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="produto",
            name="codigo",
            field=models.IntegerField(default=1, verbose_name="Código"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="produto",
            name="marca",
            field=models.ForeignKey(
                default=1,
                help_text="Selecione a marca",
                on_delete=django.db.models.deletion.PROTECT,
                to="cadastros.marca",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cliente",
            name="nome",
            field=models.CharField(max_length=50, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="produto",
            name="categoria",
            field=models.ForeignKey(
                help_text="Selecione a categoria",
                on_delete=django.db.models.deletion.PROTECT,
                to="cadastros.categoria",
            ),
        ),
        migrations.AlterField(
            model_name="produto",
            name="fornecedor",
            field=models.ForeignKey(
                help_text="Selecione o fornecedor",
                on_delete=django.db.models.deletion.PROTECT,
                to="cadastros.fornecedor",
            ),
        ),
        migrations.AlterField(
            model_name="produto",
            name="valor",
            field=models.DecimalField(
                decimal_places=2, max_digits=9, verbose_name="Valor"
            ),
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
                ("quantidade", models.FloatField(max_length=5)),
                ("cadastrado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cadastros.cliente",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        help_text="Selecione um Produto",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cadastros.produto",
                    ),
                ),
            ],
        ),
    ]