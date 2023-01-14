from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.db import models

# Create your models here.


class userManager(BaseUserManager):
    def create_user(self, firstName, lastName, email, password):
        if not email:
            raise ValueError("Users must have an email address.")
        if not firstName:
            raise ValueError("Users must have a first name.")
        if not lastName:
            raise ValueError("Users must have a last name.")
        user = self.model(
            email=self.normalize_email(email), firstName=firstName, lastName=lastName
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstName, lastName, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = userManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstName", "lastName"]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Product(models.Model):
    manufacturer = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    colors = models.CharField(max_length=128)
    storage = models.CharField(max_length=128)
    price = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    storage = models.CharField(max_length=64)
    color = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user.email}: {self.product.manufacturer} {self.product.model} - {self.color}, {self.storage}"
