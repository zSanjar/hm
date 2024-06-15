from django.contrib import admin

from app.models import Product, Images, AttributeValue, AttributeKey, ProductAttribute

# Register your models here.
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(AttributeKey)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)
