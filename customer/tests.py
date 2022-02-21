from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from customer.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('dashboard')
        self.assertEqual(resolve(url).func,dashboard)

    def test_case_register_url(self):
        url=reverse('register')
        self.assertEqual(resolve(url).func,register)

    def test_case_login_url(self):
        url=reverse('login')
        self.assertEqual(resolve(url).func,login_redirect)

    def test_case_profile_url(self):
        url=reverse('profile')
        self.assertEqual(resolve(url).func,profile)

    def test_case_logout_url(self):
        url=reverse('logout')
        self.assertEqual(resolve(url).func,logout)

    def test_case_update_url(self):
        url=reverse('update',args=[3])
        self.assertEqual(resolve(url).func,update)

class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_register_GET(self):
        response=self.client.get(reverse('register'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'auth/registration.html')

    def test_login_GET(self):
        response=self.client.get(reverse('login'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'auth/login.html')
    
    def test_dashboard_GET(self):
        response=self.client.get(reverse('dashboard'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'customer/dashboard.html')
