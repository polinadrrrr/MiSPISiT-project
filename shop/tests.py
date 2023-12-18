from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import Product, Payment, Order, OrderItem

# Create your tests here.
class TestDataBase(TestCase):
    fixtures = ['shop/fixtures/dump.json']

    def setUp(self):
        self.user = User.objects.get_or_create(username='root', password='123')
    
    def test_user_exists(self):
        self.assertTrue(User.objects.filter(username='admin').exists())

    def test_product_exists(self):
        self.assertTrue(Product.objects.filter(name='Pillow').exists())
    
    def test_all_data_exists(self):
        self.assertGreater(Product.objects.all().count(), 0)
        self.assertTrue(Payment.objects.all().exists())
        self.assertTrue(Order.objects.all().exists())
        self.assertTrue(OrderItem.objects.all().exists())

    def find_cart_number(self):
        cart_number = Order.objects.filter(user=self.user, status=Order.STATUS_CART).count()
        return cart_number
    
    def test_function_get_cart(self):
        pass
        
        self.assertEqual(self.find_cart_number(), 0)

        Order.get_cart(self.user)
        self.assertEqual(self.find_cart_number(), 1)
        
        Order.get_cart(self.user)
        self.assertEqual(self.find_cart_number(), 1)
    
    def test_cart_older_7_days(self):
        cart = Order.get_cart(self.user)
        cart.creation_time = cart.creation_time - datetime.timedelta(days=7)
        cart.save()
        cart = Order.get_cart(self.user)
        self.assertEqual(timezone.now() - cart.creation_time, datetime.timedelta(days=7))