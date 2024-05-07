from django.urls import path
from . import views
from .views import CategoriaCreate, CategoriaDelete, CategoriaDetail, CategoriaList, CategoriaUpdate, ClienteCreate, ClienteDelete, ClienteDetail, ClienteList, ClienteUpdate, FabricanteCreate, FabricanteDelete, FabricanteDetail, FabricanteList, FabricanteUpdate, FornecedorCreate, FornecedorUpdate, FornecedorList, FornecedorDelete, FornecedorDetail, FuncionarioCreate, FuncionarioDelete, FuncionarioDetail, FuncionarioList, FuncionarioUpdate, MarcaCreate, MarcaDelete, MarcaDetail, MarcaList, MarcaUpdate, ProdutoCreate, ProdutoDelete, ProdutoDetail, ProdutoList, ProdutoUpdate
from .views import ProdutoPedidoList
from .views import ClienteCreate, ClienteUpdate, ClienteList, ClienteDelete
from .views import PedidoCreate, PedidoList, PedidoDelete
from .views import CarrinhoCreate, CarrinhoList, CarrinhoUpdate, CarrinhoDelete
from .views import ClienteAutocomplete

urlpatterns = [

    path("cadastrar/fornecedor/", FornecedorCreate.as_view(), name="cadastrar-fornecedor"),
    path("cadastrar/fabricante/", FabricanteCreate.as_view(), name="cadastrar-fabricante"),
    path("cadastrar/marca/", MarcaCreate.as_view(), name="cadastrar-marca"),
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/cliente/", ClienteCreate.as_view(), name="cadastrar-cliente"),
    path("cadastrar/funcionario/", FuncionarioCreate.as_view(), name="cadastrar-funcionario"),
    path("cadastrar/produto/", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("cadastrar/pedido", PedidoCreate.as_view(), name="cadastrar-pedido"),
    path("cadastrar/carrinho", CarrinhoCreate.as_view(), name="cadastrar-carrinho"),

    path("editar/fornecedor/<int:pk>/", FornecedorUpdate.as_view(), name="editar-fornecedor"),
    path("editar/fabricante/<int:pk>/", FabricanteUpdate.as_view(), name="editar-fabricante"),
    path("editar/marca/<int:pk>/", MarcaUpdate.as_view(), name="editar-marca"),
    path("editar/categoria/<int:pk>/", CategoriaUpdate.as_view(), name="editar-categoria"),
    path("editar/cliente/<int:pk>/", ClienteUpdate.as_view(), name="editar-cliente"),
    path("editar/funcionario/<int:pk>/", FuncionarioUpdate.as_view(), name="editar-funcionario"),
    path("editar/produto/<int:pk>/", ProdutoUpdate.as_view(), name="editar-produto"),
    path("editar/carrinho/<int:pk>/", CarrinhoUpdate.as_view(), name="editar-carrinho"),

    path("excluir/fornecedor/<int:pk>/", FornecedorDelete.as_view(), name="excluir-fornecedor"),
    path("excluir/fabricante/<int:pk>/", FabricanteDelete.as_view(), name="excluir-fabricante"),
    path("excluir/marca/<int:pk>/", MarcaDelete.as_view(), name="excluir-marca"),
    path("excluir/categoria/<int:pk>/", CategoriaDelete.as_view(), name="excluir-categoria"),
    path("excluir/cliente/<int:pk>/", ClienteDelete.as_view(), name="excluir-cliente"),
    path("excluir/funcionario/<int:pk>/", FuncionarioDelete.as_view(), name="excluir-funcionario"),
    path("excluir/produto/<int:pk>/", ProdutoDelete.as_view(), name="excluir-produto"),
    path("excluir/pedido/<int:pk>/", PedidoDelete.as_view(), name="excluir-pedido"),
    path("excluir/carrinho/<int:pk>/", CarrinhoDelete.as_view(), name="excluir-carrinho"),

    path("listar/fornecedor/", FornecedorList.as_view(), name="listar-fornecedor"),
    path("listar/fabricante/", FabricanteList.as_view(), name="listar-fabricante"),
    path("listar/marca/", MarcaList.as_view(), name="listar-marca"),
    path("listar/categoria/", CategoriaList.as_view(), name="listar-categoria"),
    path("listar/cliente/", ClienteList.as_view(), name="listar-cliente"),
    path("listar/funcionario/", FuncionarioList.as_view(), name="listar-funcionario"),
    path("listar/produto/", ProdutoList.as_view(), name="listar-produto"),
    path("listar/pedido", PedidoList.as_view(), name="listar-pedido"),
    path("listar/carrinho", CarrinhoList.as_view(), name="listar-carrinho"),
    path("listar/produtos/pedido/<int:pk_pedido>/", ProdutoPedidoList.as_view(), name="listar-produtos-pedido"),

    path("detalhar/fornecedor/<int:pk>/",
         FornecedorDetail.as_view(), name="detalhar-fornecedor"),
    path("detalhar/fabricante/<int:pk>/", FabricanteDetail.as_view(), name="detalhar-fabricante"),
    path("detalhar/marca/<int:pk>/", MarcaDetail.as_view(), name="detalhar-marca"),
    path("detalhar/categoria/<int:pk>/", CategoriaDetail.as_view(), name="detalhar-categoria"),
    path("detalhar/cliente/<int:pk>/", ClienteDetail.as_view(), name="detalhar-cliente"),
    path("detalhar/funcionario/<int:pk>/", FuncionarioDetail.as_view(), name="detalhar-funcionario"),
    path("detalhar/produto/<int:pk>/", ProdutoDetail.as_view(), name="detalhar-produto"),

    #Ajax

    path("listar_produtos/", views.listar_produtos, name="listar_produtos"),
    path("buscar/cliente", ClienteAutocomplete.as_view(), name="buscar-cliente")
]
