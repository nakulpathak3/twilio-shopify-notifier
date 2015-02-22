from django.shortcuts import render
from shopify_auth.decorators import login_required, anonymous_required
from twilio.rest import TwilioRestClient
import twilio.twiml
from making_call import make_call
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json, shopify
# Create your views here.

@csrf_exempt
@login_required
def home (request, *args, **kwargs):
        #collect = shopify.Collect.find()
        #orders = shopify.Order.find()

    products = []
    with request.user.session:
        products = shopify.Product.find()
        webhook_created = False
        if not webhook_created:
            shopify.Webhook.create({"topic": "orders/create", "address": "http://4f5bf394.ngrok.com/order_webhook/","format": "json"})
            webhook_created = True
        #post_data = {"topic": "orders/create", "address": "http://requestb.in/16x1uw11","format": "json"}
        #print urllib2.urlopen('http://%s/admin/webhooks.json' % request.user, urllib.urlencode(post_data))

    for product in products:
        i = 0;
        for i in range(0, len(product.variants)):
            if product.variants[i].inventory_management == "shopify" and product.variants[i].inventory_quantity < 10:
                make_call(product.title.replace(" ", "-"))
            i += 1

    return render(request, "shopify_app/home.html", {
        'products': products,
        #'collect': collect,
        #'orders': orders,
        })

@csrf_exempt
def webhook (request, *args, **kwargs):
    if request.method == "POST":
        print "What"
        products = []

        user_model = get_user_model()

        try:
            user = user_model.objects.get(myshopify_domain = request.META['HTTP_X_SHOPIFY_SHOP_DOMAIN'])
        except user_model.DoesNotExist:
            return HttpResponse(status = 400)

        with user.session:
            products = shopify.Product.find()

        line_items = json.loads(request.body)["line_items"]

        for product in products:
            i = 0;
            make_call("product")
            for i in range(0, len(product.variants)):
                if (line_items[i]["variant_id"] == product.variants[i].id and product.variants[i].inventory_management == "shopify" and product.variants[i].inventory_quantity < 10):
                    make_call(product.title.replace(" ", "-"))

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

