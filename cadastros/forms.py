from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ["produto", "cliente", "quantidade"]

        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione um produto'}),
            'cliente': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione um cliente'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Informe a quantidade'}),
        }