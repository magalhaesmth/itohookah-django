from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15, verbose_name="WhatsApp")
    documento = models.CharField(max_length=18, help_text="Informe o CNPJ")

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.documento})"
    
class Fabricante(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.fornecedor})"
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpfCnpj = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.EmailField(max_length=300)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.cpfCnpj})"
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    endereco = models.EmailField(max_length=300)
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.usuario})"
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.FloatField(max_length=50)
    valor = models.EmailField(max_length=20)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.quantidade})"

    
 #Fazer um para Origem do Produto = importado ou não, da onde veio pa
 