from django.contrib import admin
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, Wishlist, ProductImages, ProductReview, Address


# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ["user", "title", "product_image", "price", "featured", "product_status"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_image"]


class VendorAdmin(admin.ModelAdmin):
    list_display = ["title", "vendor_image"]

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ["order", "product_status", "item", "image", "qty", "price", "total"]

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "invoice_no", "price", "paid_status", "product_status", "order_date"]


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review", "rating"]

class WishlistAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "date"]

class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "status"]



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)