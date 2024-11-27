from dal import autocomplete
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Carrinho, Pedido, Produto, Categoria, Fornecedor, Cliente
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

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
                    'data-placeholder': 'Informe o nome do cliente...',
                    'data-minimum-input-length': 2,
                },
            )
        }

class CarrinhoForm(forms.ModelForm):
    class Meta:
            model = Carrinho
            fields = ["produto", "quantidade"]
            widgets = {
                'produto': autocomplete.ModelSelect2(
                    url='buscar-produto',
                    attrs={
                        'data-placeholder': 'Informe o nome do produto...',
                        'data-minimum-input-length': 2,
                    },
                ),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('produto', css_class='col-md-10'),
                Column('quantidade', css_class='col-md-2'),
            )
        )

class ProdutoFilterForm(forms.Form):
    nome = forms.CharField(required=False, label='Nome')
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False, label='Categoria')
    fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all(), required=False, label='Fornecedor')

class PedidoFilterForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=False, label="Cliente")
    valor_min = forms.DecimalField(required=False, label="Valor Mínimo", min_value=0, decimal_places=2)
    valor_max = forms.DecimalField(required=False, label="Valor Máximo", min_value=0, decimal_places=2)
    data_inicio = forms.DateField(required=False, label="Data de Início", widget=AdminDateWidget)
    data_fim = forms.DateField(required=False, label="Data de Fim", widget=AdminDateWidget)