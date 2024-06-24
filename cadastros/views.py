from typing import Any, Dict
from .models import Categoria, Cliente, Fabricante, Fornecedor, Funcionario, Marca, Produto, Pedido, Carrinho, ProdutoPedido
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render
from dal import autocomplete
from .forms import PedidoForms, ProdutoForms

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

#Framework de mensagens/notificações
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class FornecedorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Fornecedor
    fields = ["nome", "telefone"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-fornecedor")
    extra_context = {"titulo": "Cadastro de Fornecedores"}
    success_message = "Fornecedor %(nome)s foi cadastrado com sucesso!"

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Fornecedor"
        return dados

class FabricanteCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Fabricante
    fields = ["nome"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-fabricante") 
    extra_context = {"titulo": "Cadastro de Fabricante"}
    success_message = "Fabricante %(nome)s foi cadastrado com sucesso!"

class MarcaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Marca
    fields = ["nome", "fornecedor"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-marca")
    extra_context = {"titulo": "Cadastro de Marca"}
    success_message = "Marca %(nome)s foi cadastrado com sucesso!"

class CategoriaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-categoria")
    extra_context = {"titulo": "Cadastro de Categoria"}
    success_message = "Categoria %(nome)s foi cadastrado com sucesso!"

class ClienteCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cliente
    fields = ["nome", "cpfCnpj", "telefone", "cep", "logradouro", "numero", "bairro", "cidade"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-cliente")
    extra_context = {"titulo": "Cadastro de Cliente"}
    success_message = "Cliente %(nome)s foi cadastrado com sucesso!"

class FuncionarioCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Funcionario
    fields = ["nome", "email", "funcao", "endereco", "telefone"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-funcionario")
    extra_context = {"titulo": "Cadastro de Funcionario"}
    success_message = "Funcionário %(nome)s foi cadastrado com sucesso!"

    #Método executado ao submeter um formulario
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        url = super().form_valid(form)
        return url

class ProdutoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Produto
    fields = ["codigo", "nome", "valor", "quantidade", "fornecedor", "marca", "categoria"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-produto")
    extra_context = {"titulo": "Cadastro de Produto"}
    success_message = "Produto %(nome)s foi cadastrado com sucesso!"

class PedidoCreate(LoginRequiredMixin, CreateView):
    form_class = PedidoForms
    template_name = "cadastros/form-pedido.html"
    success_url = reverse_lazy("listar-pedido")
    extra_context = {"titulo": "Cadastro de Pedido"}

    def form_valid(self, form):
        form.instance.valor_total = 0.0

        # cria a venda no banco e o object
        url = super().form_valid(form)

        # faz um select em todos os produtos do carirnho
        produtos_pedido = Carrinho.objects.all()
        valor_total = 0.0

        if (produtos_pedido.count() == 0):
            form.add_error("", "Seu carrinho de compras está vazio!")
            return super().form_invalid(form)

        for i in produtos_pedido:
            valor_total += (float(i.produto.valor) * i.quantidade)

            ProdutoPedido.objects.create(
                produto=i.produto,
                pedido=self.object,
                preco=i.produto.valor * i.quantidade,
                quantidade=i.quantidade
            )

            i.delete()

        self.object.valor_total = valor_total
        self.object.save()

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carrinho = Carrinho.objects.all()
        total_itens = sum(item.quantidade for item in carrinho)
        valor_total = sum(item.quantidade * item.produto.valor for item in carrinho)
        
        context["carrinho"] = carrinho
        context["total_itens"] = total_itens
        context["valor_total"] = valor_total

        return context


class CarrinhoCreate(LoginRequiredMixin, CreateView):
    model = Carrinho
    fields = ["produto", "quantidade"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-carrinho")
    extra_context = {"titulo": "Adicionar item ao Carrinho"}


#######################################################################################

class FornecedorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Fornecedor
    fields = ["nome", "telefone"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-fornecedor")
    success_message = "Fornecedor %(nome)s foi atualizado com sucesso!"

class FabricanteUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Fabricante
    fields = ["nome"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-fabricante")
    success_message = "Fabricante %(nome)s foi atualizado com sucesso!"

class MarcaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Marca
    fields = ["nome", "fornecedor"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-marca")
    success_message = "Marca %(nome)s foi atualizado com sucesso!"

class CategoriaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-categoria")
    success_message = "Categoria %(nome)s foi atualizado com sucesso!"

class ClienteUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cliente
    fields = ["nome", "cpfCnpj", "telefone", "cep", "logradouro", "numero", "bairro", "cidade"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-cliente")
    success_message = "Cliente %(nome)s foi atualizado com sucesso!"

class FuncionarioUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Funcionario
    fields = ["nome", "email", "funcao", "endereco", "telefone"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-funcionario")
    success_message = "Funcionário %(nome)s foi atualizado com sucesso!"

class ProdutoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Produto
    fields = ["codigo", "nome", "valor", "quantidade", "fornecedor", "marca", "categoria"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-produto")
    success_message = "Produto %(nome)s foi atualizado com sucesso!"

class CarrinhoUpdate(LoginRequiredMixin, UpdateView):
    model = Carrinho
    fields = ["produto", "quantidade"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-carrinho")

######################################################################################

class FornecedorDelete(LoginRequiredMixin, DeleteView):      
    model = Fornecedor
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-fornecedor")

class FabricanteDelete(LoginRequiredMixin, DeleteView):  
    model = Fabricante
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-fabricante")

class MarcaDelete(LoginRequiredMixin, DeleteView):  
    model = Marca
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-marca")

class CategoriaDelete(LoginRequiredMixin, DeleteView):  
    model = Categoria
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-categoria")

class ClienteDelete(LoginRequiredMixin, DeleteView):  
    model = Cliente
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-cliente")

class FuncionarioDelete(LoginRequiredMixin, DeleteView):  
    model = Funcionario
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-funcionario")

class ProdutoDelete(LoginRequiredMixin, DeleteView):  
    model = Produto
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-produto")

class PedidoDelete(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-pedido")

class CarrinhoDelete(LoginRequiredMixin, DeleteView):
    model = Carrinho
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-carrinho")

######################################################################################

class FornecedorList(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = "cadastros/list/fornecedor.html"
    paginate_by = 10 

    def get_queryset(self):
        return Fornecedor.objects.all()

class FabricanteList(LoginRequiredMixin, ListView):
    model = Fabricante
    template_name = "cadastros/list/fabricante.html"
    paginate_by = 10 

    def get_queryset(self):
        return Fornecedor.objects.all()

class MarcaList(LoginRequiredMixin, ListView):
    model = Marca
    template_name = "cadastros/list/marca.html"

class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "cadastros/list/categoria.html"

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "cadastros/list/cliente.html"

class FuncionarioList(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = "cadastros/list/funcionario.html"


class ProdutoList(LoginRequiredMixin, ListView):
    model = Produto
    template_name = "cadastros/list/produto.html"
    paginate_by = 10 

    def get_queryset(self):
        return Produto.objects.select_related('marca__fornecedor', 'categoria').all()

class PedidoList(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = "cadastros/list/pedido.html"
    paginate_by = 50

    # Melhora no desempenho da consulta, isso é um INNER JOIN no atributo CLIENTE
    def get_queryset(self):
        return Pedido.objects.all().select_related("cliente")


class CarrinhoList(LoginRequiredMixin, ListView):
    model = Carrinho
    template_name = "cadastros/list/carrinho.html"
    paginate_by = 50


class ProdutoPedidoList(LoginRequiredMixin, ListView):
    model = ProdutoPedido
    template_name = "cadastros/list/produto-pedido.html"

    def get_queryset(self):
        return ProdutoPedido.objects.filter(pedido__pk=self.kwargs["pk_pedido"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        pedido = Pedido.objects.get(pk=self.kwargs["pk_pedido"])
        produtos_pedido = self.get_queryset()
        
        total_itens = sum(item.quantidade for item in produtos_pedido)
        valor_total = sum(item.preco for item in produtos_pedido)
        
        context["pedido"] = pedido
        context["total_itens"] = total_itens
        context["valor_total"] = valor_total

        return context

######################################################################################

class FornecedorDetail(LoginRequiredMixin, DetailView):
    model = Fornecedor
    template_name = "cadastros/detail/Fornecedor.html"

class FabricanteDetail(LoginRequiredMixin, DetailView):
    model = Fornecedor
    template_name = "cadastros/detail/fabricante.html"

class MarcaDetail(LoginRequiredMixin, DetailView):
    model = Marca
    template_name = "cadastros/detail/marca.html"

class CategoriaDetail(LoginRequiredMixin, DetailView):
    model = Categoria
    template_name = "cadastros/detail/categoria.html"

class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = "cadastros/detail/cliente.html"

class FuncionarioDetail(LoginRequiredMixin, DetailView):
    model = Funcionario
    template_name = "cadastros/detail/funcionario.html"

class ProdutoDetail(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = "cadastros/detail/produto.html"

#############################################################################################
# Ajax

def listar_produtos(request):
    produtos = Produto.objects.all()
    data = [{'codigo': produto.codigo, 'nome': produto.nome, 'valor': str(produto.valor), 'quantidade': produto.quantidade, 'fornecedor': produto.fornecedor.nome, 'marca': produto.marca.nome, 'categoria': produto.categoria.nome} for produto in produtos]
    return JsonResponse({'produtos': data})

######################################## AUTOCOMPLETE ########################################


class ClienteAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        object_list = Cliente.objects.all()

        if self.q:
            object_list = object_list.filter(
                nome__icontains=self.q
            )

        return object_list
