from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views
from rpg.models import *
from rpg.views import *

#Test models

# Test case In the area of the user profile
class UserManagementTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("testUsername", "test@gmail.com", "testPassword")
        UserProfile.objects.create(user=user)

    def testUserExists(self):
        # Test that the new user exists
        user = User.objects.get(username="testUsername")
        UserProfile.objects.get(user=user)

        # Test that the number of users is 1
        self.assertEqual(1, UserProfile.objects.count(), "Number of Profiles must be 1")

    def testLogIn(self):
        login = self.client.login(username='testUsername', password='testPassword')
        self.assertTrue(login)

#Test views
