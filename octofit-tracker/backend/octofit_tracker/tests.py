from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        # Clear the User table before each test
        User.objects.all().delete()

    def test_create_user(self):  # Method name starts with "test_"
        # Create a user using Django ORM
        user = User.objects.create(email="test@example.com", name="Test User")

        # Retrieve the user from the database
        retrieved_user = User.objects.get(email="test@example.com")
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "test@example.com")
        self.assertEqual(retrieved_user.name, "Test User")

    def test_get_users(self):  # Method name starts with "test_"
        # Create multiple users
        User.objects.create(email="user1@example.com", name="User One")
        User.objects.create(email="user2@example.com", name="User Two")

        # Retrieve all users
        users = User.objects.all()
        self.assertEqual(users.count(), 2)

        # Verify the details of the users
        user1 = users.get(email="user1@example.com")
        user2 = users.get(email="user2@example.com")
        self.assertEqual(user1.name, "User One")
        self.assertEqual(user2.name, "User Two")