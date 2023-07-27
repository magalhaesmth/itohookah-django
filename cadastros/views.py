from cadastros.forms import VendaForm
from .models import Categoria, Cliente, Fabricante, Fornecedor, Funcionario, Marca, Produto, Venda
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class FornecedorCreate(LoginRequiredMixin, CreateView):
    model = Fornecedor
    fields = ["nome", "telefone"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-fornecedor")
    extra_context = {"titulo": "Cadastro de Fornecedores"}


    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Fornecedor"
        return dados

class FabricanteCreate(LoginRequiredMixin, CreateView):
    model = Fabricante
    fields = ["nome"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-fabricante") 
    extra_context = {"titulo": "Cadastro de Fabricante"}

class MarcaCreate(LoginRequiredMixin, CreateView):
    model = Marca
    fields = ["nome", "fornecedor"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-marca")
    extra_context = {"titulo": "Cadastro de Marca"}

class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-categoria")
    extra_context = {"titulo": "Cadastro de Categoria"}


class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["nome", "cpfCnpj", "telefone", "endereco"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-cliente")
    extra_context = {"titulo": "Cadastro de Cliente"}

class FuncionarioCreate(LoginRequiredMixin, CreateView):
    model = Funcionario
    fields = ["nome", "email", "funcao", "endereco", "telefone"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-funcionario")
    extra_context = {"titulo": "Cadastro de Funcionario"}

    #Método executado ao submeter um formulario
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        url = super().form_valid(form)
        return url

class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ["nome", "valor", "codigo", "fornecedor", "marca", "categoria"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-produto")
    extra_context = {"titulo": "Cadastro de Produto"}

class VendaCreate(LoginRequiredMixin, CreateView):
    model = Venda
    form_class = VendaForm
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-venda")
    extra_context = {"titulo": "Venda"}

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        url = super().form_valid(form)
        return url


#######################################################################################

class FornecedorUpdate(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    fields = ["nome", "telefone"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-fornecedor")

class FabricanteUpdate(LoginRequiredMixin, UpdateView):
    model = Fabricante
    fields = ["nome"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-fabricante")

class MarcaUpdate(LoginRequiredMixin, UpdateView):
    model = Marca
    fields = ["nome", "fornecedor"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-marca")

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-categoria")

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ["nome", "cpfCnpj", "telefone", "endereco"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-cliente")

class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
    model = Funcionario
    fields = ["nome", "email", "funcao", "endereco", "telefone"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-funcionario")

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ["nome", "valor", "codigo", "fornecedor", "marca", "categoria"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-produto")

class VendaUpdate(LoginRequiredMixin, UpdateView):
    model = Venda
    fields = ["produto", "cliente", "quantidade"]
    template_name = "cadastros/form-cadastros.html"
    success_url = reverse_lazy("listar-venda")


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

class VendaDelete(LoginRequiredMixin, DeleteView):  
    model = Venda
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-venda")


######################################################################################

class FornecedorList(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = "cadastros/list/fornecedor.html"

class FabricanteList(LoginRequiredMixin, ListView):
    model = Fabricante
    template_name = "cadastros/list/fabricante.html"

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

class VendaList(LoginRequiredMixin, ListView):
    model = Venda
    template_name = "cadastros/list/venda.html"

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

class VendaDetail(LoginRequiredMixin, DetailView):
    model = Venda
    template_name = "cadastros/detail/venda.html"
