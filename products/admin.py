from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models
from .models import Product

# Register your models here.
admin.site.register (Product)