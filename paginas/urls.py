from django.urls import path
from .views import IndexView, SobreView, RelatoriosView

urlpatterns = [
    path("", IndexView.as_view(), name="pagina-inicial"),

    path("sobre", SobreView.as_view(), name="sobre"),

    path("relatorios", RelatoriosView.as_view(), name="relatorios"),
]