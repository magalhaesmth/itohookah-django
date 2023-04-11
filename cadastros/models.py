from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    documento = models.CharField(max_length=18, help_text="Informe o CNPJ")

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | CNPJ: ({self.documento})"
    
class Fabricante(models.Model):
    nome = models.CharField(max_length=50)
    
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome}"

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome}"
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome}"

class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    cpfCnpj = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=300)

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | CPF: {self.cpfCnpj} | Telefone: {self.telefone}"
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    funcao = models.CharField(max_length=50)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=15)

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | Função: {self.funcao}"
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Valor")
    codigo = models.IntegerField(verbose_name="Código")
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.PROTECT, help_text="Selecione o fornecedor")
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, help_text="Selecione a marca")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, help_text="Selecione a categoria")

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | R${self.valor} | Código: {self.codigo} | Marca: {self.marca}"
    
class Venda(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.PROTECT, help_text="Selecione um Produto")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    quantidade = models.FloatField(max_length=5)

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.produto} | {self.quantidade}"
 
 #Fazer um para Origem do Produto = importado ou não, da onde veio pa
 