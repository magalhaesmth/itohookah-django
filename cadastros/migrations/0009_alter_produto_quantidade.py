# Generated by Django 4.1.5 on 2023-08-25 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0008_produto_quantidade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="quantidade",
            field=models.IntegerField(default=0, verbose_name="Quantidade"),
        ),
    ]
