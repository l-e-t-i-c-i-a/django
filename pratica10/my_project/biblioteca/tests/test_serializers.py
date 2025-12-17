from django.test import TestCase
from ..serializers import AutorSerializer, LivroSerializer
from ..models import Autor, Editora
from datetime import date

class SerializerTest(TestCase):

    def setUp(self):
        self.autor = Autor.objects.create(nome="Autor Teste")
        self.editora = Editora.objects.create(nome="Companhia dos Testes")

    def test_autor_serializer_validacao_customizada(self):
        """Testa o método validate_nome do AutorSerializer"""
        # Caso inválido (valor '0')
        dados_invalidos = {'nome': '0'}
        serializer = AutorSerializer(data=dados_invalidos)
        self.assertFalse(serializer.is_valid())
        self.assertIn('Validação teste', str(serializer.errors['nome']))

        # Caso válido
        dados_validos = {'nome': 'Aldous Huxley'}
        serializer = AutorSerializer(data=dados_validos)
        self.assertTrue(serializer.is_valid())

    def test_livro_serializer_output(self):
        """Verifica se os campos do Livro saem no formato correto (Serialização)"""
        livro_dados = {
            'isbn': '9000000000000',
            'autor': self.autor.id,
            'editora': self.editora.id,
            'titulo': 'Teste',
            'publicacao': date(2025, 10, 12),
            'preco': '29.90',
            'estoque': 50
        }
        serializer = LivroSerializer(data=livro_dados)
        self.assertTrue(serializer.is_valid())
        
        # O 'id' deve estar presente no dicionário de saída (data)
        # mesmo que não tenha sido enviado, após o save() ou se passado instância
        self.assertEqual(serializer.validated_data['titulo'], 'Teste')