from django.db import models

# Create your models here.


class MainCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20)
    addressline1 = models.CharField(max_length=100)
    addressline2 = models.CharField(max_length=100)
    addressline3 = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="images/",
                            default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20)
    addressline1 = models.CharField(max_length=100)
    addressline2 = models.CharField(max_length=100)
    addressline3 = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="images/",
                            default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ShopProduct(models.Model):
    mainCategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.IntegerField()
    promotion_price = models.IntegerField()
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    stock = models.CharField(max_length=20)
    description = models.TextField()

    pic1 = models.ImageField(upload_to="images/",
                             default=None, blank=True, null=True)
    pic2 = models.ImageField(upload_to="images/",
                             default=None, blank=True, null=True)
    pic3 = models.ImageField(upload_to="images/",
                             default=None, blank=True, null=True)
    pic4 = models.ImageField(upload_to="images/",
                             default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    promotion_price = models.IntegerField()
    image = models.URLField()
    quantity = models.IntegerField()
    subtotal = models.IntegerField()


# pip install pillow ...... to upload images in database
