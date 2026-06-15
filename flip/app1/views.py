from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, Purchase


def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'products.html',
        {'products': products}
    )

def add_to_cart(request, product_id):
    customer = "Murthy"

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        customer_name=customer,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

def view_cart(request):
    customer = "Murthy"

    cart_items = Cart.objects.filter(
        customer_name=customer
    )

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return render(
        request,
        'cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )

def purchase(request):
    customer = "Murthy"

    cart_items = Cart.objects.filter(customer_name=customer)

    for item in cart_items:

        if item.quantity > item.product.stock:
            return render(
                request,
                'cart.html',
                {
                    'cart_items': cart_items,
                    'error': f"{item.product.name} has insufficient stock."
                }
            )

    for item in cart_items:

        Purchase.objects.create(
            customer_name=customer,
            product=item.product,
            quantity=item.quantity,
            total_amount=item.product.price * item.quantity
        )

        item.product.stock -= item.quantity
        item.product.save()

    cart_items.delete()

    return render(
    request,
    'success.html',
    {
        'message': 'Order placed successfully!'
    }
    )

def remove_from_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)

    item.delete()

    return redirect('view_cart')