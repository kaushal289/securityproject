from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from customer.views import *
from product.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('product_create')
        self.assertEqual(resolve(url).func,product_create)

    def test_case_product_create_url(self):
        url=reverse('product_create',args=[3])
        self.assertEqual(resolve(url).func,product_create)
    
    def test_case_editproduct_create_url(self):
        url=reverse('editproduct',args=[3])
        self.assertEqual(resolve(url).func,editproduct)
    
    def test_case_product_create_url(self):
        url=reverse('productupdate',args=[3])
        self.assertEqual(resolve(url).func,productupdate)
    
    

class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_product_create_GET(self):
        response=self.client.get(reverse('product_create'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'admin/addproduct.html')

