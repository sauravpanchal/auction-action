import datetime
from unicodedata import category 
from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length = 35)
    address = models.TextField(blank = False)
    contact = models.IntegerField()
    email = models.EmailField(blank = False)
    bid_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length = 35)
    address = models.TextField(blank = False)
    contact = models.IntegerField()
    email = models.EmailField(blank = False)
    sell_count = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)
    total = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 255, null = False, blank = False)
    seller_id = models.ForeignKey(Seller, blank = False, on_delete = models.CASCADE)
    buyer_id = models.ForeignKey(Buyer, null = True, blank = True, on_delete = models.DO_NOTHING)
    category_id = models.ForeignKey(Category, blank = False, on_delete = models.DO_NOTHING)
    total_bids = models.IntegerField(default = 0)
    total_likes = models.IntegerField(default = 0)
    start_time = models.DateTimeField(default = datetime.datetime.now())
    end_time = models.DateTimeField(default = datetime.datetime.now() + datetime.timedelta(days = 3))
    price = models.IntegerField()
    status = models.CharField(max_length = 10, default = 'Live')

    def __str__(self):
        return self.name

class Bid(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    buyer_id = models.ForeignKey(Buyer, on_delete = models.CASCADE)
    amount = models.IntegerField(null = False, blank = False)
    bid_time = models.DateTimeField(default = datetime.datetime.now())
    status = models.CharField(default = 'Pending', max_length = 20)

    def __str__(self):
        return str(self.product_id)

class WishlistItem(models.Model):
    buyer_id = models.ForeignKey(Buyer, blank = False, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, blank = False, on_delete = models.CASCADE)
    category_id = models.ForeignKey(Category, blank = False, on_delete = models.DO_NOTHING)

    def __str__(self):
        return str(self.product_id)