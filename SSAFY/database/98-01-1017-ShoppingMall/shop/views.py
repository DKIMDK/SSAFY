from django.shortcuts import render, redirect
from .models import Product, Hashtag
import requests

# Create your views here.
def index(request):
    response = requests.get("https://fakestoreapi.com/products")
    products = response.json()
    
    # 반복하면서 저장
    for product in products:
        # 이미 저장된 상품이면 pass
        if Product.objects.filter(title=product['title']).exists():
            continue
        title = product['title']
        description = product['description']
        price = int(product['price'] * 1300)
        image = product['image']
        Product.objects.create(
            title = title,
            description = description,
            price = price,
            image = image,
        )
    context = {
        # 'products': products, 
        'products': Product.objects.all(),
    }
    return render(request, 'shop/index.html', context)

def addcart(request, product_pk):
    product = Product.objects.get(id=product_pk)
    user = request.user

    if product in user.cart.all():
        user.cart.remove(product)
    else:
        user.cart.add(product)
    
    return redirect("shop:index")

def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    products = hashtag.product_set.order_by('-pk')
    context = {
        'hashtag': hashtag,
        'products': products,
    }
    return render(request, 'shop/hashtag.html', context)