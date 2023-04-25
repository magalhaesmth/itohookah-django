from django.urls import path
from .views import FornecedorCreate, FornecedorUpdate, FornecedorList, FornecedorDelete, FornecedorDetail


urlpatterns = [

    path("cadastrar/fornecedor/", FornecedorCreate.as_view(), name="cadastrar-fornecedor"),

    path("editar/fornecedor/<int:pk>/", FornecedorUpdate.as_view(), name="editar-fornecedor"),

    path("excluir/fornecedor/<int:pk>/", FornecedorDelete.as_view(), name="excluir-fornecedor"),

    path("listar/fornecedor/", FornecedorList.as_view(), name="listar-fornecedor"),

    path("detalhar/fornecedor/<int:pk>/",
         FornecedorDetail.as_view(), name="detalhar-fornecedor"),
]
