from os import name
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, name, email, username, password=None,**extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(name=name, email=email, username=username, password=password)

class CustomUser(AbstractUser): 
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=[("seller", "Seller"),("buyer","Buyer"), ("admin", "Admin")], default="buyer")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username


class manageProperties(models.Model):
    PropertyType=[
        ('APARTMENT' ,'AP'),
        ('HOUSE', 'HS'),
        ('COMMERCIAL ', 'CM'),
        ('LAND ', 'LD'),
    ]
    # Basic Details
    title = models.CharField(max_length=200, help_text="Short title for the property")
    description = models.TextField(help_text="Detailed description of the property")
    property_type = models.CharField(
        max_length=50,
        choices=PropertyType,
        help_text="Type of the property",
    )
    price = models.DecimalField(max_digits=12, decimal_places=2, help_text="Price in your currency")
    size = models.DecimalField(max_digits=10, decimal_places=2, help_text="Size in square meters")

    address = models.CharField(max_length=255, help_text="Property address")
    city = models.CharField(max_length=100, help_text="City where the property is located")
    state = models.CharField(max_length=100, help_text="State or region of the property")
    zip_code = models.CharField(max_length=10, help_text="Postal/Zip code")
    country = models.CharField(max_length=100, default="India", help_text="Country")
    
    image = models.ImageField(upload_to='property_images/', null=True, blank=True, help_text="Main image of the property")
