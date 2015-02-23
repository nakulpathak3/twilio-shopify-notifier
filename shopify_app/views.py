from django.shortcuts import render
from shopify_auth.decorators import login_required, anonymous_required
from twilio.rest import TwilioRestClient
from making_call import make_call
from sending_sms import send_text
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json, shopify, twilio.twiml
from django import forms
# Create your views here.

#Problems:
# 1. If 2 or more line items in order that have inventory less than 10, you'll get two consecutive calls
# 2. Voice mail? Send a text as well? - DONE.
# 3. Inventory not tracked, app will be useless to customer.
# 4. If guy cancels order, no webhook for that and inventory goes above 10, should probably call customer
# 5. Let the user decide when to call
# 6. if csalled once, dont call everytime it goes below 10
# 7. Separate for all products
# 8. Give option to receive call/text
# 9. Which item from inventory are you talking about bro?

@login_required
def home (request, *args, **kwargs):

    products = []
    with request.user.session:
        products = shopify.Product.find()

        webhook_created = False

        if not webhook_created:
            shopify.Webhook.create({
                "topic": "orders/create",
                "address": "https://nakul-shopify.ngrok.com/webhook_created/",
                "format": "json"})

    return render(request, "shopify_app/home.html", {
        'products': products,
        })

called_once = False

@csrf_exempt
def webhook (request, *args, **kwargs):
    if request.method == "POST":
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
            for i in range(0, len(product.variants)):

                if (line_items[i]["variant_id"] == product.variants[i].id
                        and product.variants[i].inventory_management == "shopify"
                        and product.variants[i].inventory_quantity < 10):

                    make_call(product.title.replace(" ", "-"))
                    send_text(product.title.replace(" ", "-"))

        called_once = True # If I called when inventory was at 9, no need to call again and again as it
        # goes down
        return HttpResponse(status=200)

    elif request.method == "GET":
        return render(request, "shopify_app/order_webhook.html")

@csrf_exempt
def twilio_call(request, product_name=""):
    resp = twilio.twiml.Response()
    resp.say("Hello, your product %s has less than 10 items left in inventory." % product_name)
    return HttpResponse(str(resp))

# Client ID = f5ce9a546ecb08809ff2516679be471e

