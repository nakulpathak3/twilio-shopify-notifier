from django.shortcuts import render
from shopify_auth.decorators import login_required
# Create your views here.

@login_required
def home (request, *args, **kwargs):
    products = []

    import shopify
    with request.user.session:
        products = shopify.Product.find()

    return render(request, "shopify_app/home.html", {
        'products': products,
        })
