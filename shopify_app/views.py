from django.shortcuts import render
from shopify_auth.decorators import login_required
from twilio.rest import TwilioRestClient
from making_call import make_call
# Create your views here.

@login_required
def home (request, *args, **kwargs):
    products = []

    import shopify
    with request.user.session:
        products = shopify.Product.find()
        #collect = shopify.Collect.find()
        #orders = shopify.Order.find()

    for product in products:
        if product.id == 41511613:
            make_call()

    return render(request, "shopify_app/home.html", {
        'products': products,
        #'collect': collect,
        #'orders': orders,
        })

# I can access:
    # collections
    # products

