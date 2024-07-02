from django.contrib import admin
from .models import *


# class CategoryAdmin(admin.ModelAdmin):
#     list_display =('name','description')



admin.site.register(Category)
admin.site.register(Product)