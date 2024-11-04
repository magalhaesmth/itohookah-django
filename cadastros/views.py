from .models import Categoria, Cliente, Fabricante, Fornecedor, Funcionario, Marca, Produto, Pedido, Carrinho, ProdutoPedido
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render, redirect
from dal import autocomplete
from .forms import CarrinhoForm, PedidoForms, ProdutoFilterForm, PedidoFilterForm

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
    fields = ["nome", "valor", "quantidade", "fornecedor", "marca", "categoria", "imagem"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-produto")
    extra_context = {"titulo": "Cadastro de Produto"}
    success_message = "Produto %(nome)s foi cadastrado com sucesso!"

class PedidoCreate(LoginRequiredMixin, CreateView):
    form_class = PedidoForms
    template_name = "cadastros/form-pedido.html"
    success_url = reverse_lazy("listar-pedido")
    extra_context = {"titulo": "Fechar Pedido"}

    def form_valid(self, form):
        form.instance.valor_total = 0.0

         # Faz um select em todos os produtos do carirnho
        produtos_pedido = Carrinho.objects.all()
        valor_total = 0.0

        if (produtos_pedido.count() == 0):
            form.add_error("", "Seu carrinho de compras está vazio!")
            return super().form_invalid(form)

        semestoque = []
        for i in produtos_pedido:
            if(i.quantidade>i.produto.quantidade):
                semestoque.append(f"{i.produto.nome} ({i.produto.quantidade})")

        if(len(semestoque)>0):
            form.add_error("", f"Estoque indisponível para: {str(semestoque)}")
            return super().form_invalid(form)

        # Cria a venda no banco e o object
        url = super().form_valid(form)

        for i in produtos_pedido:
            valor_total += (float(i.produto.valor) * i.quantidade)

            ProdutoPedido.objects.create(
                produto=i.produto,
                pedido=self.object,
                preco=i.produto.valor * i.quantidade,
                quantidade=i.quantidade
            )

            i.produto.quantidade-=i.quantidade
            i.produto.save()

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
    form_class = CarrinhoForm
    template_name = "cadastros/form-carrinho.html"
    success_url = reverse_lazy("cadastrar-pedido")
    extra_context = {"titulo": "Adicionar item ao Carrinho"}

    def form_valid(self, form):
        item = Carrinho.objects.filter(produto = form.instance.produto)
        if(item.exists()):
            item[0].quantidade += form.instance.quantidade
            item[0].save()
            
            return redirect(self.success_url)
        
        if(form.instance.produto.quantidade < form.instance.quantidade):
            form.add_error("produto", "Este produto não possui a quantidade desejada!")
            form.add_error("quantidade", f"O produto {form.instance.produto.nome} possui em estoque: {form.instance.produto.quantidade}")
            return super().form_invalid(form)
        
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carrinho = Carrinho.objects.all()
        total_itens = sum(item.quantidade for item in carrinho)
        valor_total = sum(item.quantidade * item.produto.valor for item in carrinho)
        
        context["carrinho"] = carrinho
        context["total_itens"] = total_itens
        context["valor_total"] = valor_total

        return context


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
    fields = ["nome", "valor", "quantidade", "fornecedor", "marca", "categoria", "imagem"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-produto")
    success_message = "Produto %(nome)s foi atualizado com sucesso!"

class CarrinhoUpdate(LoginRequiredMixin, UpdateView):
    model = Carrinho
    fields = ["produto", "quantidade"]
    template_name = "cadastros/form-carrinho.html"
    success_url = reverse_lazy("cadastrar-pedido")
    extra_context = {"titulo": "Editar item do carrinho"}

    def form_valid(self, form):
        if form.cleaned_data['quantidade'] <= 0:
            form.add_error('quantidade', 'A quantidade deve ser maior que 0.')
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carrinho = Carrinho.objects.all()
        total_itens = sum(item.quantidade for item in carrinho)
        valor_total = sum(item.quantidade * item.produto.valor for item in carrinho)
        
        context["carrinho"] = carrinho
        context["total_itens"] = total_itens
        context["valor_total"] = valor_total

        return context
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
    success_url = reverse_lazy("cadastrar-carrinho")

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ProdutoFilterForm(self.request.GET)
        context['filter_form'] = form
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = ProdutoFilterForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data.get('nome'):
                queryset = queryset.filter(nome__icontains=form.cleaned_data['nome'])
            if form.cleaned_data.get('categoria'):
                queryset = queryset.filter(categoria=form.cleaned_data['categoria'])
            if form.cleaned_data.get('fornecedor'):
                queryset = queryset.filter(fornecedor=form.cleaned_data['fornecedor'])
        return queryset

class PedidoList(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = "cadastros/list/pedido.html"
    paginate_by = 50

    def get_queryset(self):
        queryset = Pedido.objects.all().select_related("cliente").order_by('-criado_em')
        cliente = self.request.GET.get('cliente')
        valor_min = self.request.GET.get('valor_min')
        valor_max = self.request.GET.get('valor_max')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')

        if cliente:
            queryset = queryset.filter(cliente__id=cliente)
        if valor_min:
            queryset = queryset.filter(valor_total__gte=valor_min)
        if valor_max:
            queryset = queryset.filter(valor_total__lte=valor_max)
        if data_inicio:
            queryset = queryset.filter(criado_em__date__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(criado_em__date__lte=data_fim)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = PedidoFilterForm(self.request.GET or None)
        context['form'] = form
        
        pedidos = self.get_queryset()

        # Adiciona a quantidade total e o valor total para todos os pedidos filtrados
        total_itens_geral = 0
        valor_total_geral = 0

        for pedido in pedidos:
            produtos_pedido = pedido.produtopedido_set.all()
            pedido.total_itens = sum(item.quantidade for item in produtos_pedido)
            pedido.valor_total = sum(item.quantidade * item.produto.valor for item in produtos_pedido)

            # Somar os itens e o valor total geral
            total_itens_geral += pedido.total_itens
            valor_total_geral += pedido.valor_total

        # Adiciona os totais gerais no contexto
        context["total_itens_geral"] = total_itens_geral
        context["valor_total_geral"] = valor_total_geral
        context["pedidos"] = pedidos

        return context



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
    data = [{'nome': produto.nome, 'valor': str(produto.valor), 'quantidade': produto.quantidade, 'fornecedor': produto.fornecedor.nome, 'marca': produto.marca.nome, 'categoria': produto.categoria.nome} for produto in produtos]
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
