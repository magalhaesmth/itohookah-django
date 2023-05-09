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
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-fornecedor")
    extra_context = {"titulo": "Cadastro de Fornecedores"}


    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Fornecedor"
        return dados

class FabricanteCreate(CreateView):
    model = Fabricante
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-fabricante") 
    extra_context = {"titulo": "Cadastro de Fabricante"}

class MarcaCreate(CreateView):
    model = Marca
    fields = ["nome", "fornecedor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")
    extra_context = {"titulo": "Cadastro de Marca"}

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")
    extra_context = {"titulo": "Cadastro de Categoria"}


class ClienteCreate(CreateView):
    model = Cliente
    fields = ["nome", "cpfCnpj", "telefone", "endereco"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")
    extra_context = {"titulo": "Cadastro de Cliente"}

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome", "email", "funcao", "endereco", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")
    extra_context = {"titulo": "Cadastro de Funcionario"}

class ProdutoCreate(CreateView):
    model = Produto
    fields = ["nome", "valor", "codigo", "fornecedor", "marca", "categoria"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")
    extra_context = {"titulo": "Cadastro de Produto"}

class VendaCreate(CreateView):
    model = Venda
    fields = ["produto", "cliente", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-venda")
    extra_context = {"titulo": "Cadastro de Venda"}


#######################################################################################

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ["nome", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-fornecedor")

class FabricanteUpdate(UpdateView):
    model = Fabricante
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-fabricante")

class MarcaUpdate(UpdateView):
    model = Marca
    fields = ["nome", "fornecedor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ["nome", "cpfCnpj", "telefone", "endereco"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ["nome", "email", "funcao", "endereco", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ["nome", "valor", "codigo", "fornecedor", "marca", "categoria"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")

class VendaUpdate(UpdateView):
    model = Venda
    fields = ["produto", "cliente", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-venda")


######################################################################################

class FornecedorDelete(DeleteView):      
    model = Fornecedor
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-fornecedor")

class FabricanteDelete(DeleteView):
    model = Fabricante
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-fabricante")

class MarcaDelete(DeleteView):
    model = Marca
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-marca")

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-categoria")

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-cliente")

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-funcionario")

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-produto")

class VendaDelete(DeleteView):
    model = Venda
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-venda")


######################################################################################

class FornecedorList(ListView):
    model = Fornecedor
    template_name = "cadastros/list/fornecedor.html"

class FabricanteList(ListView):
    model = Fabricante
    template_name = "cadastros/list/fabricante.html"

class MarcaList(ListView):
    model = Marca
    template_name = "cadastros/list/marca.html"

class CategoriaList(ListView):
    model = Categoria
    template_name = "cadastros/list/categoria.html"

class ClienteList(ListView):
    model = Cliente
    template_name = "cadastros/list/cliente.html"

class FuncionarioList(ListView):
    model = Funcionario
    template_name = "cadastros/list/funcionario.html"

class ProdutoList(ListView):
    model = Produto
    template_name = "cadastros/list/produto.html"

class VendaList(ListView):
    model = Venda
    template_name = "cadastros/list/venda.html"

######################################################################################

class FornecedorDetail(DetailView):
    model = Fornecedor
    template_name = "cadastros/detail/Fornecedor.html"

class FabricanteDetail(DetailView):
    model = Fornecedor
    template_name = "cadastros/detail/fabricante.html"

class MarcaDetail(DetailView):
    model = Marca
    template_name = "cadastros/detail/marca.html"

class CategoriaDetail(DetailView):
    model = Categoria
    template_name = "cadastros/detail/categoria.html"

class ClienteDetail(DetailView):
    model = Cliente
    template_name = "cadastros/detail/cliente.html"

class FuncionarioDetail(DetailView):
    model = Funcionario
    template_name = "cadastros/detail/funcionario.html"

class ProdutoDetail(DetailView):
    model = Produto
    template_name = "cadastros/detail/produto.html"

class VendaDetail(DetailView):
    model = Venda
    template_name = "cadastros/detail/venda.html"
