from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CookModelTest(TestCase):
    def test_cook_creation(self):
        cook = get_user_model().objects.create_user(
            username="chef_marcus",
            password="SecurePassword123!",
            years_of_experience=10,
            first_name="Marcus",
            last_name="Griswold",
        )
        self.assertEqual(cook.username, "chef_marcus")
        self.assertEqual(cook.years_of_experience, 10)
        self.assertEqual(cook.first_name, "Marcus")
        self.assertEqual(cook.last_name, "Griswold")


class CookViewsTest(TestCase):
    def setUp(self):
        self.signup_url = reverse("signup")

    def test_signup_page_accessible(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)

    def test_signup_valid_data(self):
        data = {
            "username": "new_chef",
            "password1": "Password5566!",
            "password2": "Password5566!",
            "years_of_experience": 4,
            "first_name": "John",
            "last_name": "Doe",
        }
        response = self.client.post(self.signup_url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            get_user_model().objects.filter(username="new_chef").exists()
        )
