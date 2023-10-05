from django import template

register = template.Library()

# Exemplos de tags e filtros genéricas que podem ser utilizadas

@register.filter(name="desconto_10")
def desconto_10(valor):
    return valor * 0.9

@register.filter(name="remover")
def remover(texto, sai):
    return texto.replace(sai, "")

@register.simple_tag(name="substituir")
def substituir(texto, sai, entra):
    return texto.replace(sai, entra)