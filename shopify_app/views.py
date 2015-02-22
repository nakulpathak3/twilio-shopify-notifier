from django.shortcuts import render
from shopify_auth.decorators import login_required, anonymous_required
from twilio.rest import TwilioRestClient
import twilio.twiml
from making_call import make_call
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
# Create your views here.

@login_required
def home (request, *args, **kwargs):
        #collect = shopify.Collect.find()
        #orders = shopify.Order.find()

    products = []

    import shopify
    with request.user.session:
        products = shopify.Product.find()

    for product in products:
        i = 0;
        for i in range(0, len(product.variants)):
            if product.variants[i].inventory_management == "shopify" and product.variants[i].inventory_quantity < 10:
                print product.title.replace(" ","-")
                make_call(product.title.replace(" ", "-"))
            i += 1

    return render(request, "shopify_app/home.html", {
        'products': products,
        #'collect': collect,
        #'orders': orders,
        })

@csrf_exempt
@login_required
def webhook (request, *args, **kwargs):
    if request.method == "POST":

        products = []
        print "I got here"

        import shopify
        with request.user.session:
            products = shopify.Product.find()

        line_items = json.loads(request.body)["line_items"]
        for i in range(0, len(line_items)):
            print line_items[i]["variant_id"]

        for product in products:
            i = 0;
            for i in range(0, len(product.variants)):
                if (line_items[i]["variant_id"] == product.variants[i].id and product.variants[i].inventory_management == "shopify" and product.variants[i].inventory_quantity < 10):
                    make_call()

        return HttpResponse(status=200)

    elif request.method == "GET":
        return render(request, "shopify_app/order_webhook.html")

@csrf_exempt
def twilio_call(request, product_name=""):
    resp = twilio.twiml.Response()
    resp.say("Hello, your product %s has less than 10 items left in inventory." % product_name)
    return HttpResponse(str(resp))
# The problem is that I want to access the products in a client's store when a webhook comes in
# The thing is I can't ask the webhook to login
# But if the user has already logged in and has the app installed, shouldn't it not matter?
# Assuming it doesn't matter, once I get the product

# Client ID = f5ce9a546ecb08809ff2516679be471e

