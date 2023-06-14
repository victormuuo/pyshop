from django.contrib import admin
from .models import Product,offer


class offerAdmin(admin.ModelAdmin):
    list_display=('code','discount')


admin.site.register(offer,offerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')

# Register your models here.
admin.site.register(Product,ProductAdmin)