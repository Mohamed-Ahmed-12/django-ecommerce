from django.shortcuts import redirect, render
from products.models import Product
from .models import OrderProduct 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name='redirect', login_url='/account/login')    
def add_product(request):
    user = User.objects.get(username=request.user) # get user
    product_id = int(request.GET.get('pro_id'))
    product_quantity = int(request.GET.get('pro_qty'))
    product = Product.objects.get(id=product_id) # get product from database
    if OrderProduct.objects.filter(user=user , product=product).exists():
        print("TRUE**************************************")
        order_product = OrderProduct.objects.filter(user=user , product=product )
        order_product.update(quantity = product_quantity )
        #order_product.save()
    else:
        print("FALSE**************************************")
        order_product = OrderProduct.objects.create(user=user , product=product ,quantity = product_quantity )
        #order_product.save()
    return render(request , 'parts/store.html')

def get_product_order(request):
    if request.user.is_authenticated:
        products = OrderProduct.objects.filter(user=request.user)
        count = products.count()
        request.session['count'] = count # session
        return render(request , 'cart/cart.html' ,context={'products':products })
    else:
        return render(request , 'cart/cart.html' )

def remove_product(request):
    product_id = int(request.GET.get('pro_id'))
    product = OrderProduct.objects.get(user = request.user,id = product_id).delete()
    return render(request , 'cart/cart.html')

