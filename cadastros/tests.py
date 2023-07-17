from django.test import TestCase
import unittest
import re

# Como usuario do sistema, preciso realizar o login com uma senha segura
# Para isso, a senha deve conter comprimento minimo de 8 caracteres válidos, um numero, uma ou mais letras minusculas e uma letra maiuscula.
# Utilizando nome das funções com underline (_) para seguir o padrão da biblioteca unittest

# Re é a biblioteca Regex.

def validar_senha(senha):
    if len(senha) != 8:
        return False

    if not re.search('[A-Z]', senha):
        return False

    if not re.search('[a-z]', senha):
        return False

    if not re.search('[0-9]', senha):
        return False

    return True

# Resumindo essa função, se tiver os parametros necessários, retorna true, se não tiver qualquer outro
# parâmetro, retorna false.

class TestSenha(unittest.TestCase):
    def test_senha_valida(self):
        senha = "Matheus123"
        resultado = validar_senha(senha)
        self.assertTrue(resultado)
    # Senha válida, tem 10 caracteres, numero e letra maiuscula

    def test_comprimento_minimo(self):
        senha = "Mgl321"
        resultado = validar_senha(senha)
        self.assertFalse(resultado)
    # Senha inválida, menos de 10 caracteres

    def test_sem_letras_maiuscula(self):
        senha = "matheus123"
        resultado = validar_senha(senha)
        self.assertFalse(resultado)
    # Senha inválida, não tem letra maiuscula

    def test_sem_letras_minuscula(self):
        senha = "MATHEUSMGL"
        resultado = validar_senha(senha)
        self.assertFalse(resultado)
    # Senha invalida, não tem letra minuscula

    def test_sem_numeros(self):
        senha = "Matheusmgl"
        resultado = validarSenha(senha)
        self.assertFalse(resultado)
    # Senha invalida, não tem numeros

if __name__ == '__main__':
    unittest.main()
