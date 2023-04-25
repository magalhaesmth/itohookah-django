from .models import Fornecedor
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


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ["nome", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-fornecedor")


class FornecedorDelete(DeleteView):
    model = Fornecedor
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("deletar-fornecedor")

class FornecedorList(ListView):
    model = Fornecedor
    template_name = "cadastros/list/fornecedor.html"

class FornecedorDetail(DetailView):
    model = Fornecedor
    template_name = "cadastros/detail/Fornecedor.html"
