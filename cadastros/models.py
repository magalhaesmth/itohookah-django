from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    documento = models.CharField(max_length=18, help_text="Informe o CNPJ")

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome}"
    
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
    cep = models.CharField(max_length=10, verbose_name="CEP")
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, verbose_name="Número", null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50)

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

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | Função: {self.funcao}"
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Valor")
    quantidade = models.IntegerField(verbose_name="Quantidade", default=0)
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.PROTECT, help_text="Selecione o fornecedor")
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, help_text="Selecione a marca")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, help_text="Selecione a categoria")
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True, verbose_name="Imagem")

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | R${self.valor} |  Marca: {self.marca}"
    
class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT)
    valor_total = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Preço")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


class ProdutoPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    preco = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Preço")
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.produto.nome} ({self.quantidade})'

class Carrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Produto: {self.produto} | Qtd. {self.quantidade}'

    
#=======================================================================================
# Ajax 



 #Fazer um para Origem do Produto = importado ou não, da onde veio pa
 