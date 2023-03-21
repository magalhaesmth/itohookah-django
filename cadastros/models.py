from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15, verbose_name="WhatsApp")
    documento = models.CharField(max_length=18, help_text="Informe o CNPJ")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.documento})"
    

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.fornecedor})"
    
 #Fazer um para Origem do Produto = importado ou não, da onde veio pa