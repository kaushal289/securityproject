from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from buyproduct.views import *
from customer.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_bill_create_url(self):
        url=reverse('bill_create')
        self.assertEqual(resolve(url).func,bill_create)

    def test_case_yourproduct_url(self):
        url=reverse('yourproduct')
        self.assertEqual(resolve(url).func,yourproduct)

    def test_case_buypage_url(self):
        url=reverse('buypage',args=[3])
        self.assertEqual(resolve(url).func,buypage)

    def test_case_updatedelete_url(self):
        url=reverse('updatedelete',args=[3])
        self.assertEqual(resolve(url).func,updatedelete)


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_bill_create_GET(self):
        response=self.client.get(reverse('register'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'buypages/buymainpage.html')


