from django.contrib import admin
# from .models import Product, Images

# admin.site.register(Product)

# admin.site.register(Images)


# from .models import Post, PostImage
from .models import Product, Images

class ImagesAdmin(admin.StackedInline):
    model = Images
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]
 
    class Meta:
       model = Product
 
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass