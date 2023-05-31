from django.test import TestCase
from users.models import User

from .models import Ingredient, Recipe, Tag


class IngredientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ingredient.objects.create(name='Соль', measurement_unit='г')

    def test_name_label(self):
        ingredient = Ingredient.objects.get(id=1)
        field_label = ingredient._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Название')

    def test_measurement_unit_label(self):
        ingredient = Ingredient.objects.get(id=1)
        field_label = ingredient._meta.get_field(
            'measurement_unit'
        ).verbose_name
        self.assertEqual(field_label, 'Единица измерения')

    def test_name_max_length(self):
        ingredient = Ingredient.objects.get(id=1)
        max_length = ingredient._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_measurement_unit_max_length(self):
        ingredient = Ingredient.objects.get(id=1)
        max_length = ingredient._meta.get_field('measurement_unit').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name(self):
        ingredient = Ingredient.objects.get(id=1)
        expected_object_name = (
            f'{ingredient.name}, {ingredient.measurement_unit}'
        )
        self.assertEqual(expected_object_name, str(ingredient))


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(
            name='Test Tag', color='#FF0000', slug='test-tag'
        )

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, 'Test Tag')
        self.assertEqual(self.tag.color, '#FF0000')
        self.assertEqual(self.tag.slug, 'test-tag')


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='testuser', password='testpass')
        Ingredient.objects.create(
            name='Test Ingredient', measurement_unit='g.'
        )
        Tag.objects.create(name='Test Tag')

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            name='Test Recipe',
            author=User.objects.get(username='testuser'),
            text='This is a test recipe.',
            image='test_image.jpg',
            cooking_time=10,
        )
        self.assertEqual(recipe.name, 'Test Recipe')
        self.assertEqual(recipe.author, User.objects.get(username='testuser'))
        self.assertEqual(recipe.text, 'This is a test recipe.')
        self.assertEqual(recipe.image, 'test_image.jpg')
        self.assertEqual(recipe.cooking_time, 10)

    def test_recipe_tags(self):
        recipe = Recipe.objects.create(
            name='Test Recipe',
            author=User.objects.get(username='testuser'),
            text='This is a test recipe.',
            image='test_image.jpg',
            cooking_time=10,
        )
        tag = Tag.objects.get(name='Test Tag')
        recipe.tags.add(tag)
        self.assertIn(tag, recipe.tags.all())
