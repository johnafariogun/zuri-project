# importing relevant classes i'm  using User cause it is better than creating a custom user which might be more stressful
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # importing the user attributes from User and setting on_delete to cascade to delete all items associated to the user
    url = models.CharField(max_length=700) # creating a url field for the ecommerce apps
    max_price = models.FloatField() # creating a price field so that we can alert the user for price change
    

