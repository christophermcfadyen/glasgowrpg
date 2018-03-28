import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowRPG.settings')
django.setup()

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import views as auth_views
from rpg.models import *
from rpg.views import *
import unittest
from django.test import Client
from PIL import Image



class SimpleTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_addition(self):

        # Ensure that tests are working
        self.assertEqual(1 + 2, 3)


class StaticFileTests(TestCase):

    def test_static_files(self):

        # test if logo is printed
        result = finders.find('images/logo1.png')
        self.assertIsNotNone(result)





#Page Tests, response , templates and message display
class AboutPageTest(TestCase):

    def test_about_response(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)


    def test_about_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'rpg/about.html')

    def test_about_contains_message(self):
        response = self.client.get(reverse('about'))
        self.assertIn(b'Glasgow RPG is a free to play', response.content)


class HelpPageTest(TestCase):

    def test_help_response(self):
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)

    def test_help_template(self):
        response = self.client.get(reverse('help'))
        self.assertTemplateUsed(response, 'rpg/help.html')

class HomePageTest(TestCase):

    def test_home_response(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'rpg/home.html')

class LoginPageTest(TestCase):

    def test_login_response(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'rpg/login.html')

class PlayPageTest(TestCase):

    def test_play_response_without_login(self):
        response = self.client.get(reverse('play'))
        self.assertEqual(response.status_code, 302)
        
    #login required
    def test_play_template(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('play'))
        self.assertTemplateUsed(response, 'rpg/play.html')

class RegisterPageTest(TestCase):

    def test_register_response(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'rpg/register.html')


class StatsPageTest(TestCase):

    def test_stats_response_without_login(self):
        response = self.client.get(reverse('stats'))
        self.assertEqual(response.status_code, 302)
        
    #login required
    def test_stats_template(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('stats'))
        self.assertTemplateUsed(response, 'rpg/stats.html')

class UserprofilePageTest(TestCase):

    def test_userprofile_response_without_login(self):
        response = self.client.get(reverse('userprofile'))
        self.assertEqual(response.status_code, 302)
        
    #login required
    def test_userprofile_template(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('userprofile'))
        self.assertTemplateUsed(response, 'rpg/userprofile.html')


#Test for user section of the web app

class UserManagementTest(TestCase):

    def setUp(self):
        user = User.objects.create_user("testUsername", "test@gmail.com", "testPassword")
        UserProfile.objects.create(user=user)

    def testUserExists(self):

        user = User.objects.get(username="testUsername")
        UserProfile.objects.get(user=user)

        self.assertEqual(1, UserProfile.objects.count(), "Number of Profiles must be 1")

    def testLogIn(self):
        login = self.client.login(username='testUsername', password='testPassword')
        self.assertTrue(login)










