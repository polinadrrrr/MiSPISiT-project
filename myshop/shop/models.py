from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])
    
class User(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])
    

class Order(models.Model):
    customer = models.CharField(max_length=255)
    phone = models.CharField(max_length=200, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=255, choices=[('online', 'Online'), ('offline', 'Offline')])
    status = models.CharField(max_length=255, choices=[('active', 'Active'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return self.customer
    
    def get_absolute_url(self):
        return f'/{self.customer}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    discount = models.FloatField(default=0)
    cost = models.FloatField()


    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return f'/{self.product.slug}'
