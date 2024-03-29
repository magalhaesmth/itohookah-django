# Generated by Django 4.2.7 on 2023-11-23 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0009_alter_produto_quantidade"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="bairro",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="cliente",
            name="cep",
            field=models.CharField(default=1, max_length=10, verbose_name="CEP"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cliente",
            name="cidade",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cliente",
            name="logradouro",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cliente",
            name="numero",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Número"
            ),
        ),
    ]
