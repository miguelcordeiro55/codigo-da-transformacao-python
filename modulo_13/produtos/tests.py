from django.test import TestCase
from .models import Produto

class ProdutoTest(TestCase):

    def test_criar_produto(self):
        produto = Produto.objects.create(
            nome='Teste',
            descricao='Produto teste',
            preco=10.00,
            quantidade=5
        )
        self.assertEqual(produto.nome, 'Teste')
