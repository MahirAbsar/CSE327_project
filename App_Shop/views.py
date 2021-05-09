from django.shortcuts import render,HttpResponse

# Import views
from django.views.generic import ListView, DetailView

# Models
from App_Shop.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.




class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'

def Search(request):
    item = request.GET['search-item']
    searched_product = Product.objects.filter(name__icontains=item)
    return render(request,"App_Shop/search.html",{"searched_product":searched_product})
