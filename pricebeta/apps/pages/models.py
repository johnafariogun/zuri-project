from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
# model for the various category phone brands e.g. Samsung, Iphone, Xiaomi etc. that we have can be scaled up to inlude electronics  
class Category(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

# model for the phones themselves under the different phone brands e.g. Iphone8, iphone 11 etc.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField() # probably call a function here to get the price from the web scraper but using Floatfield as a placeholder
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='static/products/')
  
    @staticmethod # staticmethod, won't be run until it is called
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)# function that can be run to retrieve products by id, the id are automatically given in the database this is a faster way of querying the database


        # argument ids will be a list or an iterable cause of the '__in' so that we can get if the id is in that list e.g [1,4,89,9] 
    @staticmethod
    def get_all_products():
        return Product.objects.all()
  

    @staticmethod # not really sure about this cause i don't know what dango will use as the primary key so may be adjusted later
    def get_all_products_by_categoryid(category_id):
        if category_id: # this is used to get the porducts by the category name so all phones in the iphone category
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.name



class WishList(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


  
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).wish_by('-date')

