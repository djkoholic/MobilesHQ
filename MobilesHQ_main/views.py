from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import User, Product, Cart
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.


def index(request):
    return render(request, "MobilesHQ_main/index.html")


def register(request):
    if request.method == "POST":
        fn = request.POST["fn"]
        ln = request.POST["ln"]
        email = request.POST["email"]
        password = request.POST["password"]
        new_user = User.objects.create_user(fn, ln, email, password)
        new_user.save()
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "MobilesHQ_main/register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request, "MobilesHQ_main/login.html", {"message": "Invalid Credentials"}
            )
    return render(request, "MobilesHQ_main/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def product(request, id):
    if request.method == "POST":
        form = request.POST
        cart = Cart(
            user=request.user,
            product=Product.objects.get(id=id),
            storage=form["Storage"],
            color=form["Color"],
        )
        cart.save()
        return HttpResponseRedirect(reverse("product", kwargs={"id": id}))
    else:
        product = Product.objects.get(id=id)
        colors = product.colors.split(",")
        colorsList = []
        colorsDict = {}
        if len(colors) == 1:
            colorsDict = {"id": 1, "color": colors, "checked": True}
            colorsList.append(colorsDict)
        else:
            i = 0
            for color in colors:
                if i == 0:
                    colorsDict = {"id": i, "color": color, "checked": True}
                else:
                    colorsDict = {"id": i, "color": color, "checked": False}
                i += 1
                colorsList.append(colorsDict)
        storageList = []
        storageDict = {}
        storage = product.storage.split(",")
        prices = product.price.split(",")
        if len(storage) == 1:
            storageDict = {
                "id": 1,
                "storage": storage,
                "price": prices,
                "checked": True,
            }
            storageList.append(storageDict)
        else:
            i = 0
            for store in storage:
                if i == 0:
                    storageDict = {
                        "id": i,
                        "storage": store,
                        "price": prices[i],
                        "checked": True,
                    }
                else:
                    storageDict = {
                        "id": i,
                        "storage": store,
                        "price": prices[i],
                        "checked": False,
                    }
                i += 1
                storageList.append(storageDict)
        return render(
            request,
            "MobilesHQ_main/product.html",
            {
                "product": product,
                "colors": colorsList,
                "storage": storageList,
            },
        )


def cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product = Product.objects.get(
            manufacturer=data["manufacturer"], model=data["model"]
        )
        cart = Cart.objects.get(
            user=request.user,
            product=product,
            color=data["color"],
            storage=data["storage"],
        )
        cart.delete()   
    cart = Cart.objects.filter(user=request.user)
    cartList = []
    cartDict = {}
    i = 0
    for product in cart:
        cartDict = {
            "id": i,
            "manufacturer": product.product.manufacturer,
            "model": product.product.model,
            "color": product.color,
            "storage": product.storage,
        }
        i += 1
        cartList.append(cartDict)
    return render(request, "MobilesHQ_main/cart.html", {"cart": cartList})
