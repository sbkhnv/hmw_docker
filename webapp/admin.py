from django.contrib import admin
from .models import Order,Category,Product


admin.site.register([Order,Category,Product])