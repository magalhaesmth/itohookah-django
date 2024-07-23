from dal import autocomplete
from django import forms
from .models import Pedido, Produto, Categoria, Fornecedor


class ProdutoForms(forms.ModelForm):
    preco = forms.DecimalField(decimal_places=2, max_digits=9, localize=True)

    class Meta:
        model = Produto
        fields = ["nome", "preco", "marca"]
    
class PedidoForms(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["cliente"]
        widgets = {
            'cliente': autocomplete.ModelSelect2(
                url='buscar-cliente',
                attrs={
                    'data-placeholder': 'Informe o nome do Cliente...',
                    'data-minimum-input-length': 3,
                },
            )
        }

class ProdutoFilterForm(forms.Form):
    nome = forms.CharField(required=False, label='Nome')
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False, label='Categoria')
    fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all(), required=False, label='Fornecedor')