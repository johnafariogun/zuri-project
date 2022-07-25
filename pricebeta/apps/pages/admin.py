from django.contrib import admin
from apps.main.models import Items
from apps.pages.models import Product,Category,WishList
# Register your models here.
admin.site.register(Items)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(WishList)