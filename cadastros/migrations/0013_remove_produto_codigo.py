# Generated by Django 5.0.4 on 2024-07-02 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0012_remove_pedido_ciclo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='codigo',
        ),
    ]