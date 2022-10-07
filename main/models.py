import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

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
    # TODO: Images (bytea [data-type], not null)
    # TODO: Description (1600 Chars)
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

# Extending UserModel
class UserAccountManager(BaseUserManager):
    def create_user(self, name, address, contact, email, type, password = None):
        if not email:
            raise ValueError("User must have an Email address")

        email = self.normalize_email(email)
        user = self.model(name = name, address = address, contact = contact, email = email, type = type)
        user.set_password(password)
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    contact = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 25, unique = True)
    type = models.CharField(max_length = 6, default = "Buyer")
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "address", "contact", "type"]

    objects = UserAccountManager()

    def get_full_name(self):
        return self.name

    def __str__(self) -> str:
        return self.email