from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
            messages.error(request, "There's nothing in your shopping cart at the moment")
            return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JKq6NFkzat2NiNoXrJtCj8X0TaHSdg9ebfxVgDM5stvIGAYA1zUFTNi9Y40f3m50ZyjCrc6ja7GWl5UCe1UPizb00V8OwpQY6',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
