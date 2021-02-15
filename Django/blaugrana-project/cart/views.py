from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product,Images
from django.utils import timezone
from django.db.models import Q


def _cart_id(request):
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart

@login_required(login_url="/accounts/login")
def add_to_cart(request, product_id):
     product = Product.objects.get(id=product_id)
     print(product.title)
     cart = None

     try:
          cart = Cart.objects.get(user_id=request.user.id)
          print('try')
     except:
          cart = Cart.objects.create(
               user_id=request.user.id,
               created_at=timezone.datetime.now()
          )
          cart.save()
          print('except')

     print(cart)
     try:
          cart_item = CartItem.objects.get(product = product, cart= cart)
          cart_item.save()
          print('try')
     except:
          cart_item = CartItem.objects.create(
               product = product,
               cart=cart
          )
          cart_item.save()
          print('except')
          
     return redirect('cart_detail')

@login_required(login_url="/accounts/login")
def cart_detail(request):
     cart = Cart.objects.filter(user_id=request.user.id).values()
     # print(cart)
     cart_id = []
     for i in cart:
          cart_id.append(i['id'])
     cart_id=cart_id[0]
     # print(cart_id)
     cartitem_initial = list(CartItem.objects.filter(cart_id=cart_id).values())
     print(cartitem_initial)
     cartitem = []
     for j in cartitem_initial:
          cartitem.append(j['product_id'])
     print(cartitem)
     products = []
     for k in cartitem:
          product = list(Product.objects.filter(id=k).values())
          # print(product)
          products.append(product[0])
     
     print(products)




     # if cartitem != []:
     #      for id in cartitem:
     #           product_id = cartitem[0]['product_id']
     #           product = list(Product.objects.filter(id=product_id).values())
     #           # product = get_object_or_404(Product,pk=product_id)
     #           products.append(product[0])
     
     # product_id = cartitem[0]['product_id']
     # product = get_object_or_404(Product,pk=product_id)
     # print(product)
     # print(products)
     # print(products[0]['products.image.url'])
     return render(request, 'cart/detail_cart.html', {'products':products})

@login_required(login_url="/accounts/login")
def remove_cart(request, product_id):
     product = Product.objects.get(id=product_id)
     cart = Cart.objects.filter(user_id=request.user.id).values()
     cart_id = []
     for i in cart:
          cart_id.append(i['id'])
     cart_id=cart_id[0]
     cart_item = CartItem.objects.filter(Q(product_id=product_id) , Q(cart_id=cart_id))
     print(cart_item)
     cart_item.delete()
     return redirect('cart_detail')