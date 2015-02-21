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
        i = 0;
        for i in range(0, len(product.variants)):
            if product.variants[i].inventory_management == "shopify" and product.variants[i].inventory_quantity < 10:
                make_call()
            i += 1

    return render(request, "shopify_app/home.html", {
        'products': products,
        #'collect': collect,
        #'orders': orders,
        })

# I can access:
    # collections
    # products

