from django.contrib import admin
from .models import Fornecedor, Fabricante, Marca, Categoria, Cliente, Funcionario, Produto, Venda

# Register your models here.
admin.site.register(Fornecedor)
admin.site.register(Fabricante)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Produto)
admin.site.register(Venda)
