from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Author
from user.models import User

class AuthorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='Test Name', birth_date='1990-01-01', bio='Test Bio', user=self.user)

    def test_author_creation(self):
        self.assertEqual(self.author.name, 'Test Name')
        self.assertEqual(str(self.author), 'Test Name')

class AuthorAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author_data = {'name': 'Test Name', 'birth_date': '1990-01-01', 'bio': 'Test Bio', 'user': self.user.id}
        self.author = Author.objects.create(**self.author_data)

    def test_author_list(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_author_detail(self):
        response = self.client.get(f'/api/authors/{self.author.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Name')

    def test_author_creation(self):
        response = self.client.post('/api/authors/', self.author_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Author.objects.count(), 2)

    def test_author_update(self):
        updated_data = {'name': 'Updated Name', 'bio': 'Updated Bio'}
        response = self.client.put(f'/api/authors/{self.author.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Updated Name')

    def test_author_deletion(self):
        response = self.client.delete(f'/api/authors/{self.author.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Author.objects.count(), 0)