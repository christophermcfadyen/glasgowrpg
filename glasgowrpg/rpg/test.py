from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views
from rpg.models import *
from rpg.views import *
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        

class SimpleMathTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        
    def test_addition(self):
        
        # Ensure that tests are working
        self.assertEqual(1 + 2, 3)


    def test_static_files(self):

        # test if logo is printed
        result = finders.find('images/logo1.png')
        self.assertIsNotNone(result)

        
#Test views   
class RpgPageResponseTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
    
    def test_about_response(self):
    response = self.client.get(reverse('about'))
    self.assertEqual(response.status_code, 200)

    def test_help_response(self):
    response = self.client.get(reverse('help'))
    self.assertEqual(response.status_code, 200)

    def test_home_response(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    
    def test_login_response(self):
    response = self.client.get(reverse('login'))
    self.assertEqual(response.status_code, 200)

    def test_play_response(self):
    response = self.client.get(reverse('play'))
    self.assertEqual(response.status_code, 200)

    def test_register_response(self):
    response = self.client.get(reverse('register'))
    self.assertEqual(response.status_code, 200)

    def test_stats_response(self):
    response = self.client.get(reverse('stats'))
    self.assertEqual(response.status_code, 200)

    def test_userprofile_response(self):
    response = self.client.get(reverse('userprofile'))
    self.assertEqual(response.status_code, 200)
















    
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
