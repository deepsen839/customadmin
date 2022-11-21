from django.shortcuts import render
from admin_interface.models import Theme
from .models import ProductCard
# Create your views here.
def homepage(request):
    theme = Theme.objects.filter(active=True).first()
    product_card_list = ProductCard.objects.all() 
    return render(request,'index.html',{'theme':theme,'product_list':product_card_list})