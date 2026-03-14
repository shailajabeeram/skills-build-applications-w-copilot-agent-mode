from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout


class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User(username='testuser', email='test@example.com', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
