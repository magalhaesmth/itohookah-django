from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from cadastros.models import Categoria, Cliente, Fabricante, Fornecedor, Funcionario, Marca, Produto, Venda

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/index.html"

class SobreView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/sobre.html"

class RelatoriosView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/relatorios.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categorias"] = Categoria.objects.filter(
            cadastrado_em__month=datetime.now().month).count()
        context["clientes"] = Cliente.objects.filter(
            cadastrado_em__month=datetime.now().month).count()
        context["marcas"] = Marca.objects.filter(
            cadastrado_em__month=datetime.now().month).count()
        context["fabricantes"] = Fabricante.objects.filter(
            cadastrado_em__month=datetime.now().month).count()
        context["forncedores"] = Fornecedor.objects.filter(
            cadastrado_em__month=datetime.now().month).count()
        context["produtos"] = Produto.objects.filter(
            cadastrado_em__month=datetime.now().month).count()

        return context
