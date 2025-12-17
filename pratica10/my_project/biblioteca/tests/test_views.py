from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from ..models import Autor, Editora, Livro
from datetime import date

class BibliotecaViewsTest(TestCase):

    def setUp(self):
        # 1. Configurar Cliente e Dados básicos
        self.client = Client()
        self.autor = Autor.objects.create(nome="Autor de Teste")
        self.editora = Editora.objects.create(nome="Editora de Teste")
        
        # 2. Criar utilizadores (Comum e Admin)
        self.user_comum = User.objects.create_user(username='comum', password='password123')
        self.user_admin = User.objects.create_user(username='admin', password='password123')
        
        # Dar permissão de adicionar livro ao admin
        content_type = ContentType.objects.get_for_model(Livro)
        permission = Permission.objects.get(codename='add_livro', content_type=content_type)
        self.user_admin.user_permissions.add(permission)

    def test_dashboard_acesso_publico(self):
        """Verifica se o dashboard carrega corretamente."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'biblioteca/dashboard.html')

    def test_listar_entidade_invalida(self):
        """Verifica se uma entidade inexistente mostra a página de erro."""
        response = self.client.get(reverse('listar', kwargs={'entidade': 'carro'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'inválida.')

    def test_listar_livros_paginados(self):
        """Verifica se a listagem de livros funciona e está com flag de paginação."""
        response = self.client.get(reverse('listar', kwargs={'entidade': 'livro'}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['is_paginated'])

    def test_criar_objeto_sem_login_redireciona(self):
        """Verifica se utilizador não logado é enviado para o login ao tentar criar."""
        url = reverse('criar', kwargs={'entidade': 'livro'})
        response = self.client.get(url)
        # O @login_required redireciona (302) para a página de login
        self.assertEqual(response.status_code, 302)
        self.assertIn('/biblioteca/signin/', response.url)

    def test_criar_livro_sem_permissao_denied(self):
        """Utilizador logado mas SEM permissão 'add_livro' deve receber PermissionDenied (403)."""
        self.client.login(username='comum', password='password123')
        url = reverse('criar', kwargs={'entidade': 'livro'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403) # PermissionDenied

    def test_criar_autor_sucesso_post(self):
        """Testa a criação de um autor via POST por um utilizador logado."""
        self.client.login(username='comum', password='password123')
        url = reverse('criar', kwargs={'entidade': 'autor'})
        dados = {'nome': 'Novo Autor'}
        response = self.client.post(url, data=dados)
        
        # Após salvar, ele deve redirecionar para a lista
        self.assertRedirects(response, reverse('listar', kwargs={'entidade': 'autor'}))
        self.assertTrue(Autor.objects.filter(nome='Novo Autor').exists())

    def test_logout_apenas_via_post(self):
        """Verifica se o logout bloqueia método GET (conforme tua view)."""
        self.client.login(username='comum', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 405) # Method Not Allowed