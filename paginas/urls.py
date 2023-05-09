from django.urls import path
from .views import IndexView, SobreView

urlpatterns = [
    path("", IndexView.as_view(), name="pagina-inicial"),

    path("sobre", SobreView.as_view(), name="sobre"),
]