from django.contrib import admin
from .models import ProductCard
# Register your models here.
@admin.register(ProductCard)
class ProducCardAdmin(admin.ModelAdmin):
    class Meta:
        model=ProductCard
    list_display = ('id','logo')