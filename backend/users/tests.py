from django.db import IntegrityError
from django.test import TestCase

from .models import Subscribe, User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_unicode_representation(self):
        self.assertEqual(str(self.user), 'testuser@example.com')

    def test_user_ordering(self):
        users = User.objects.all()
        self.assertEqual(users[0], self.user)

    def test_user_verbose_name(self):
        self.assertEqual(self.user._meta.verbose_name, 'Пользователь')

    def test_user_verbose_name_plural(self):
        self.assertEqual(self.user._meta.verbose_name_plural, 'Пользователи')


class SubscribeModelTest(TestCase):
    def setUp(self):
        self.test_user1 = User.objects.create_user(
            username='testuser1',
            email='testuser@example.com',
            password='testpass1',
        )
        self.test_user2 = User.objects.create_user(
            username='testuser2',
            email='testuser@example.com',
            password='testpass2',
        )
        Subscribe.objects.create(user=self.test_user1, author=self.test_user2)

    def test_user_label(self):
        subscribe = Subscribe.objects.get(id=1)
        field_label = subscribe._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'Подписчик')

    def test_author_label(self):
        subscribe = Subscribe.objects.get(id=1)
        field_label = subscribe._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'Автор')

    def test_object_name_is_author(self):
        subscribe = Subscribe.objects.get(id=1)
        expected_object_name = f'{subscribe.author.username}'
        self.assertEqual(expected_object_name, str(subscribe))

    def test_get_absolute_url(self):
        subscribe = Subscribe.objects.get(id=1)
        self.assertEqual(subscribe.get_absolute_url(), '/subscribe/1/')

    def test_unique_subscription(self):
        test_user1 = User.objects.get(username='testuser1')
        test_user2 = User.objects.get(username='testuser2')
        with self.assertRaises(IntegrityError):
            Subscribe.objects.create(user=test_user1, author=test_user2)
