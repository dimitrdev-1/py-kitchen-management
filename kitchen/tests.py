from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Dessert")
        self.assertEqual(str(dish_type), "Dessert")

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Soup")
        dish = Dish.objects.create(
            name="Tomato Soup",
            description="Fresh tomatoes",
            price=5.50,
            dish_type=dish_type,
        )
        self.assertEqual(str(dish), "Tomato Soup")


class KitchenViewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_chef", password="Password123!"
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(name="Main")
        self.dish = Dish.objects.create(
            name="Pizza",
            description="Cheese pizza",
            price=12.00,
            dish_type=self.dish_type,
        )

    def test_index_view(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)

    def test_dish_type_list_view(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)

    def test_dish_list_view(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)

    def test_cook_list_view(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertEqual(response.status_code, 200)

    def test_dish_detail_view(self):
        response = self.client.get(
            reverse("kitchen:dish-detail", kwargs={"pk": self.dish.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_cook_detail_view(self):
        response = self.client.get(
            reverse("kitchen:cook-detail", kwargs={"pk": self.user.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_dish_type_create_view(self):
        data = {"name": "Salads"}
        response = self.client.post(reverse("kitchen:dish-type-create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(DishType.objects.filter(name="Salads").exists())

    def test_dish_create_view(self):
        data = {
            "name": "Burger",
            "description": "Beef burger",
            "price": 9.99,
            "dish_type": self.dish_type.pk,
            "cooks": [self.user.pk],
        }
        response = self.client.post(reverse("kitchen:dish-create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dish.objects.filter(name="Burger").exists())
