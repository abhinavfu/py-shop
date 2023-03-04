from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register((Product, Cart, ShopUser))

admin.site.register((MainCategory, SubCategory, Brand,
                    Seller, Buyer, ShopProduct, Cart))
