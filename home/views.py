from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import *
import os
# Create your views here.

currency = '₹'

# ------------------------------------------------------------------------------------


def checkSeller(request):
    # not giving access to Buyer
    try:
        if Seller.objects.get(username=auth.get_user(request)):
            return True
        else:
            return False
    except:
        return False

# ------------------------------------------------------------------------------------
# Home | Shop |


def home(request):
    checkS = checkSeller(request)
    try:
        buyer = Buyer.objects.get(username=auth.get_user(request))
        c = Cart.objects.filter(buyer=buyer)
    except:
        c = Cart.objects.all()
    return render(request, 'home.html', {'product': ShopProduct.objects.all(), 'cart': c, 'currency': currency, 'checkS': checkS})


def shop(request, mc, sc, br):
    checkS = checkSeller(request)
    products = ShopProduct.objects.all()
    try:
        buyer = Buyer.objects.get(username=auth.get_user(request))
        c = Cart.objects.filter(buyer=buyer)
    except:
        c = Cart.objects.all()

    # filtering all products by categories
    if mc == "All" and sc == "All" and br == "All":
        products = ShopProduct.objects.all()
    elif mc != "All" and sc == "All" and br == "All":
        products = ShopProduct.objects.filter(
            mainCategory=MainCategory.objects.get(name=mc))
    elif mc == "All" and sc != "All" and br == "All":
        products = ShopProduct.objects.filter(
            subCategory=SubCategory.objects.get(name=sc))
    elif mc == "All" and sc == "All" and br != "All":
        products = ShopProduct.objects.filter(
            brand=Brand.objects.get(name=br))
    elif mc != "All" and sc != "All" and br == "All":
        products = ShopProduct.objects.filter(
            mainCategory=MainCategory.objects.get(name=mc), subCategory=SubCategory.objects.get(name=sc))
    elif mc != "All" and sc == "All" and br != "All":
        products = ShopProduct.objects.filter(
            mainCategory=MainCategory.objects.get(name=mc), brand=Brand.objects.get(name=br))
    elif mc == "All" and sc != "All" and br != "All":
        products = ShopProduct.objects.filter(
            subCategory=SubCategory.objects.get(name=sc), brand=Brand.objects.get(name=br))
    else:
        products = ShopProduct.objects.filter(
            mainCategory=MainCategory.objects.get(name=mc), subCategory=SubCategory.objects.get(name=sc), brand=Brand.objects.get(name=br))

    mainCat = MainCategory.objects.all()
    subCat = SubCategory.objects.all()
    brand = Brand.objects.all()

    return render(request, 'shop.html', {'product': products,
                                         'mainCat': mainCat,
                                         'subCat': subCat,
                                         'brand': brand,
                                         'MC': mc, 'SC': sc, 'BR': br, 'cart': c, 'currency': currency, 'checkS': checkS})

# ------------------------------------------------------------------------------------
# Product Info


@login_required(login_url='/signin/')
def payment(request, pk):
    return render(request, 'payment.html', {'currency': currency, 'amountTotal': pk})


def productInfo(request, pk):
    p = ShopProduct.objects.all().get(id=pk)
    checkS = checkSeller(request)
    data2 = False
    try:
        buyer = Buyer.objects.get(username=auth.get_user(request))
        c = Cart.objects.filter(buyer=buyer)
        for i in c:
            if p.name == i.name:
                # if data is True item is already in cart
                data2 = True
                break
            else:
                data2 = False
    except:
        c = Cart.objects.all()

    return render(request, 'productInfo.html', {'data': p, 'cart': c, 'currency': currency, 'allready': data2, 'checkS': checkS})

# ------------------------------------------------------------------------------------
# for seller add/edit/delete products


@login_required(login_url='/signin/')
def addProduct(request):
    checkS = checkSeller(request)
    seller = Seller.objects.get(username=auth.get_user(request))
    mainCat = MainCategory.objects.all()
    subCat = SubCategory.objects.all()
    brand = Brand.objects.all()
    if request.method == "POST":

        base_price = int(request.POST['price'])
        discount = int(request.POST['discount'])
        final_price = float(base_price - (base_price*discount/100))
        p = ShopProduct(mainCategory=mainCat.get(name=request.POST['mainCat']),
                        subCategory=subCat.get(name=request.POST['subCat']),
                        brand=brand.get(name=request.POST['brand']),
                        seller=Seller.objects.get(
                            username=auth.get_user(request)),
                        name=request.POST['name'],
                        price=base_price,
                        discount=discount,
                        promotion_price=final_price,
                        color=request.POST['color'],
                        size=request.POST['size'],
                        stock=request.POST['stock'],
                        description=request.POST['description'],
                        pic1=request.FILES['pic1'],
                        pic2=request.FILES['pic2'],
                        pic3=request.FILES['pic3'],
                        pic4=request.FILES['pic4'])
        p.save()
        return redirect('/userprofile')
    return render(request, 'addproduct.html', {'user': seller, 'mainCat': mainCat, 'subCat': subCat, 'brand': brand, 'checkS': checkS})


@login_required(login_url='/signin/')
def editProduct(request, pk):
    checkS = checkSeller(request)
    seller = Seller.objects.get(username=auth.get_user(request))
    mainCat = MainCategory.objects.all()
    subCat = SubCategory.objects.all()
    brand = Brand.objects.all()
    d = ShopProduct.objects.all().get(id=pk)
    if request.method == "POST":
        base_price = int(request.POST['price'])
        discount = int(request.POST['discount'])
        final_price = float(base_price - (base_price*discount/100))

        d.mainCategory = mainCat.get(name=request.POST['mainCat'])
        d.subCategory = subCat.get(name=request.POST['subCat'])
        d.brand = brand.get(name=request.POST['brand'])
        d.seller = Seller.objects.get(
            username=auth.get_user(request))
        d.name = request.POST['name']
        d.price = base_price
        d.discount = discount
        d.promotion_price = final_price
        d.color = request.POST['color']
        d.size = request.POST['size']
        d.stock = request.POST['stock']
        d.description = request.POST['description']
        try:
            if (request.FILES.get('pic1')):
                os.remove('media/'+str(d.pic1))
                d.pic1 = request.FILES['pic1']
            if (request.FILES.get('pic2')):
                os.remove('media/'+str(d.pic2))
                d.pic2 = request.FILES['pic2']
            if (request.FILES.get('pic3')):
                os.remove('media/'+str(d.pic3))
                d.pic3 = request.FILES['pic3']
            if (request.FILES.get('pic4')):
                os.remove('media/'+str(d.pic4))
                d.pic4 = request.FILES['pic4']
        except:
            d.pic1 = request.FILES['pic1']
            d.pic2 = request.FILES['pic2']
            d.pic3 = request.FILES['pic3']
            d.pic4 = request.FILES['pic4']
        d.save()
        return redirect('/userprofile')
    return render(request, 'editproduct.html', {'user': seller, 'mainCat': mainCat, 'subCat': subCat, 'brand': brand, 'd': d, 'checkS': checkS})


@login_required(login_url='/signin/')
def delProduct(request, pk):
    d = ShopProduct.objects.all().get(id=pk)
    os.remove('media/'+str(d.pic1))
    os.remove('media/'+str(d.pic2))
    os.remove('media/'+str(d.pic3))
    os.remove('media/'+str(d.pic4))
    d.delete()
    return redirect('/userprofile')

# ------------------------------------------------------------------------------------
# Cart create/update/delete items


@login_required(login_url='/signin/')
def cart(request):
    buyer = Buyer.objects.get(username=auth.get_user(request))
    c = Cart.objects.filter(buyer=buyer)
    d = 0
    for i in c:
        d = d + i.subtotal

    subtotal = round(float(d), 2)
    shipping = round(float(20), 2)
    tax = round(float((subtotal * 8) / 100), 2)
    ordertotal = float(subtotal) + float(shipping) + float(tax)
    cartData = {'cart': c, 'currency': currency, 'payment': {
        'subtotal': subtotal, 'shipping': shipping, 'tax': tax, 'ordertotal': ordertotal}}
    return render(request, 'cart.html', cartData)


@login_required(login_url='/signin/')
def cartCreate(request, pk):
    x = ShopProduct.objects.all().get(id=pk)
    buyer = Buyer.objects.get(username=auth.get_user(request))
    q = 1
    sub = q*x.promotion_price
    # c = Cart.objects.filter(buyer=buyer)
    Cart.objects.all()
    c = Cart(buyer=buyer,
             name=x.name,
             price=x.price,
             promotion_price=x.promotion_price,
             image=x.pic1.url,
             quantity=q,
             subtotal=sub)
    c.save()
    return redirect('/cart')


@login_required(login_url='/signin/')
def cartUpdate(request, pk, update):
    u = Cart.objects.all().get(id=pk)
    ux = int(u.quantity) + int(update)

    if u.quantity > 0:
        u.quantity = ux
        u.subtotal = int(ux) * int(u.promotion_price)
        u.save()
    else:
        u.quantity = 1
        u.subtotal = 1 * int(u.promotion_price)
        u.save()
    return redirect('/cart')


@login_required(login_url='/signin/')
def cartDelete(request, pk):
    buyer = Buyer.objects.get(username=auth.get_user(request))
    c = Cart.objects.filter(buyer=buyer)
    c.get(id=pk).delete()
    return redirect('/cart')


# ------------------------------------------------------------------------------------
# Signin / Signup / Logout


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/userprofile')
        else:
            messages.error(request, " Email and Password does not match")
    return render(request, 'signin.html')


def signup(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        user = request.POST["user"]
        password = request.POST["password"]
        repassword = request.POST["rpassword"]
        if password == repassword:
            try:
                if user == "Seller":
                    Seller.objects.all()
                    # cus = create user seller
                    cus = Seller(name=f"{fname} {lname}",
                                 username=f"{fname}{lname}",
                                 email=email,
                                 user_status=user)
                    cus.save()
                else:
                    Buyer.objects.all()
                    cub = Buyer(name=f"{fname} {lname}",
                                username=f"{fname}{lname}",
                                email=email,
                                user_status=user)
                    cub.save()

                mainuser = User.objects.create_user(
                    username=f"{fname}{lname}", password=password, email=email, first_name=fname, last_name=lname)
                mainuser.save()

                try:
                    user = auth.authenticate(
                        username=f"{fname}{lname}", password=password)
                    if user is not None:
                        auth.login(request, user)
                        return redirect('/userprofile')
                except:
                    messages.success(
                        request, "Your Account has been successfully created")
                    return render(request, 'signin.html')
            except:
                messages.error(request, "Username or Email id already exsits")
                return render(request, 'signup.html')
        else:
            messages.error(request, "Password does not match")
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


@login_required(login_url='/signin/')
def logout(request):
    auth.logout(request)
    return redirect('/signin')

# ------------------------------------------------------------------------------------
# User Profile


@login_required(login_url='/signin/')
def userProfile(request):
    checkS = checkSeller(request)
    try:
        user = User.objects.get(username=auth.get_user(request))
        if user.is_superuser:
            return redirect('/admin')
        else:
            try:
                seller = Seller.objects.get(username=auth.get_user(request))
                products = ShopProduct.objects.filter(seller=seller)
                return render(request, 'userprofile.html', {'user': seller, 'product': products, 'currency': currency, 'checkS': checkS})
            except:
                buyer = Buyer.objects.get(username=auth.get_user(request))
                c = Cart.objects.filter(buyer=buyer)
                return render(request, 'userprofile.html', {'user': buyer, 'currency': currency, 'cart': c, 'checkS': checkS})
    except:
        return redirect('/signin')


@login_required(login_url='/signin/')
def editProfile(request, pk):
    checkS = checkSeller(request)
    if checkS:
        s = Seller.objects.all().get(id=pk)
    else:
        s = Buyer.objects.all().get(id=pk)

    if request.method == 'POST':
        s.name = request.POST["fname"]
        s.email = request.POST["email"]
        try:
            if (request.FILES.get('pic')):
                os.remove('media/'+str(s.pic))
                s.pic = request.FILES["pic"]
        except:
            s.pic = request.FILES["pic"]

        s.save()
        return redirect('/userprofile')
    return render(request, 'editprofile.html', {'user': s, 'checkS': checkS})

# ------------------------------------------------------------------------------------
# Payment


@login_required(login_url='/signin/')
def payment(request, pk):
    return render(request, 'payment.html', {'currency': currency, 'amountTotal': pk})
