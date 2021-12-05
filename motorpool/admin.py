from django.contrib import admin

# Register your models here.
from . import models
@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    pass