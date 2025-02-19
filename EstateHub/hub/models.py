from django.db import models
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

    # Location Details
    address = models.CharField(max_length=255, help_text="Property address")
    city = models.CharField(max_length=100, help_text="City where the property is located")
    state = models.CharField(max_length=100, help_text="State or region of the property")
    zip_code = models.CharField(max_length=10, help_text="Postal/Zip code")
    country = models.CharField(max_length=100, default="India", help_text="Country")
    
    # Media
    image = models.ImageField(upload_to='property_images/', null=True, blank=True, help_text="Main image of the property")