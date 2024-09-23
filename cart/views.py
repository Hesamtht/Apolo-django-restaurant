from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import CartItem
from menu.models import Food


def add_to_cart(request):
    food_id = request.POST.get('food_id')
    food = get_object_or_404(Food, id=food_id)

    cart = request.session.get('cart', {})

    if str(food_id) in cart:
        cart[str(food_id)] += 1
    else:
        cart[str(food_id)] = 1

    request.session['cart'] = cart

    cart_count = sum(cart.values())
    return JsonResponse({'success': True, 'cart_count': cart_count})



def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for food_id, quantity in cart.items():
        food = get_object_or_404(Food, id=food_id)
        total_price += food.price * quantity
        cart_items.append({'food': food, 'quantity': quantity})

    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})



def remove_from_cart(request, food_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        if str(food_id) in cart:
            del cart[str(food_id)]
            request.session['cart'] = cart
            total_price = sum(Food.objects.get(id=int(fid)).price * qty for fid, qty in cart.items())
            return JsonResponse({'success': True, 'total_price': total_price})
        else:
            return JsonResponse({'success': False, 'error': 'Item not found in cart.'})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})



def payment(request):
    return render(request, 'cart/payment.html')
