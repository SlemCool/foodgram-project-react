from django.test import TestCase

from .models import Ingredient


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

    def test_get_absolute_url(self):
        ingredient = Ingredient.objects.get(id=1)
        self.assertEqual(ingredient.get_absolute_url(), '/ingredients/1/')
