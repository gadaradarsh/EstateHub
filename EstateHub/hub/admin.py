from django.contrib import admin
from .models import manageProperties,CustomUser
# Register your models here.
admin.site.register(manageProperties)
admin.site.register(CustomUser)