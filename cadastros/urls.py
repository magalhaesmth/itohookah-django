from django.urls import path
from . import views
from .views import CategoriaCreate, CategoriaDelete, CategoriaDetail, CategoriaList, CategoriaUpdate, ClienteCreate, ClienteDelete, ClienteDetail, ClienteList, ClienteUpdate, FabricanteCreate, FabricanteDelete, FabricanteDetail, FabricanteList, FabricanteUpdate, FornecedorCreate, FornecedorUpdate, FornecedorList, FornecedorDelete, FornecedorDetail, FuncionarioCreate, FuncionarioDelete, FuncionarioDetail, FuncionarioList, FuncionarioUpdate, MarcaCreate, MarcaDelete, MarcaDetail, MarcaList, MarcaUpdate, ProdutoCreate, ProdutoDelete, ProdutoDetail, ProdutoList, ProdutoUpdate, VendaCreate, VendaDelete, VendaDetail, VendaList, VendaUpdate


urlpatterns = [

    path("cadastrar/fornecedor/", FornecedorCreate.as_view(), name="cadastrar-fornecedor"),
    path("cadastrar/fabricante/", FabricanteCreate.as_view(), name="cadastrar-fabricante"),
    path("cadastrar/marca/", MarcaCreate.as_view(), name="cadastrar-marca"),
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/cliente/", ClienteCreate.as_view(), name="cadastrar-cliente"),
    path("cadastrar/funcionario/", FuncionarioCreate.as_view(), name="cadastrar-funcionario"),
    path("cadastrar/produto/", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("cadastrar/venda/", VendaCreate.as_view(), name="cadastrar-venda"),

    path("editar/fornecedor/<int:pk>/", FornecedorUpdate.as_view(), name="editar-fornecedor"),
    path("editar/fabricante/<int:pk>/", FabricanteUpdate.as_view(), name="editar-fabricante"),
    path("editar/marca/<int:pk>/", MarcaUpdate.as_view(), name="editar-marca"),
    path("editar/categoria/<int:pk>/", CategoriaUpdate.as_view(), name="editar-categoria"),
    path("editar/cliente/<int:pk>/", ClienteUpdate.as_view(), name="editar-cliente"),
    path("editar/funcionario/<int:pk>/", FuncionarioUpdate.as_view(), name="editar-funcionario"),
    path("editar/produto/<int:pk>/", ProdutoUpdate.as_view(), name="editar-produto"),
    path("editar/venda/<int:pk>/", VendaUpdate.as_view(), name="editar-venda"),

    path("excluir/fornecedor/<int:pk>/", FornecedorDelete.as_view(), name="excluir-fornecedor"),
    path("excluir/fabricante/<int:pk>/", FabricanteDelete.as_view(), name="excluir-fabricante"),
    path("excluir/marca/<int:pk>/", MarcaDelete.as_view(), name="excluir-marca"),
    path("excluir/categoria/<int:pk>/", CategoriaDelete.as_view(), name="excluir-categoria"),
    path("excluir/cliente/<int:pk>/", ClienteDelete.as_view(), name="excluir-cliente"),
    path("excluir/funcionario/<int:pk>/", FuncionarioDelete.as_view(), name="excluir-funcionario"),
    path("excluir/produto/<int:pk>/", ProdutoDelete.as_view(), name="excluir-produto"),
    path("excluir/venda/<int:pk>/", VendaDelete.as_view(), name="excluir-venda"),

    path("listar/fornecedor/", FornecedorList.as_view(), name="listar-fornecedor"),
    path("listar/fabricante/", FabricanteList.as_view(), name="listar-fabricante"),
    path("listar/marca/", MarcaList.as_view(), name="listar-marca"),
    path("listar/categoria/", CategoriaList.as_view(), name="listar-categoria"),
    path("listar/cliente/", ClienteList.as_view(), name="listar-cliente"),
    path("listar/funcionario/", FuncionarioList.as_view(), name="listar-funcionario"),
    path("listar/produto/", ProdutoList.as_view(), name="listar-produto"),
    path("listar/venda/", VendaList.as_view(), name="listar-venda"),

    path("detalhar/fornecedor/<int:pk>/",
         FornecedorDetail.as_view(), name="detalhar-fornecedor"),
    path("detalhar/fabricante/<int:pk>/", FabricanteDetail.as_view(), name="detalhar-fabricante"),
    path("detalhar/marca/<int:pk>/", MarcaDetail.as_view(), name="detalhar-marca"),
    path("detalhar/categoria/<int:pk>/", CategoriaDetail.as_view(), name="detalhar-categoria"),
    path("detalhar/cliente/<int:pk>/", ClienteDetail.as_view(), name="detalhar-cliente"),
    path("detalhar/funcionario/<int:pk>/", FuncionarioDetail.as_view(), name="detalhar-funcionario"),
    path("detalhar/produto/<int:pk>/", ProdutoDetail.as_view(), name="detalhar-produto"),
    path("detalhar/venda/<int:pk>/", VendaDetail.as_view(), name="detalhar-venda"),

    #Ajax

    path("listar_produtos/", views.listar_produtos, name="listar_produtos"),
    path('venda/', views.venda, name='venda'),

]
