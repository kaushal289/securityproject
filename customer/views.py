
from django.shortcuts import redirect, render
from customer.forms import CustomerForm
from customer.models import Customer
from product.models import Product
from useradmin.models import Useradmin
from django.contrib.auth import login,logout
from django.contrib import messages,auth
from authenticate import Authentication



# Create your views here.
def register(request):
    if request.method == "POST":
        print(request.POST)
        form = CustomerForm(request.POST)
        form.save()
        user1=form.cleaned_data.get('username')
        messages.success(request,"Welcome "+user1+", please login here to shop with heavy discount $$$.")
        return redirect("/login")
    else:
        form = CustomerForm()
    return render(request, "auth/registration.html", {'form': form})

def login_redirect(request):
    if request.method=='POST':
        print(request)
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            customer=Customer.objects.get(username=username,password=password)
            request.session['username']=request.POST['username']
            request.session['password']=request.POST['password']
            request.session['customer_id']=customer.customer_id
            return redirect ('/')
        except:
            user=Useradmin.objects.get(username=username,password=password)
            if user is not None:
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password'] 
                return redirect('/useradmin/admindash')
            return render("/login_redirect")
    else:
        form=CustomerForm()
        print("invalid")
    return render(request,"auth/login.html",{'form':form})  
    
@Authentication.valid_user
def profile(request):
    users=Customer.objects.get(customer_id=request.session['customer_id'])
    return render(request,"customer/profile.html",{'users':[users]})

def dashboard(request):
    swals=Product.objects.raw("select * from product where product_type='Swal'")
    sweeters=Product.objects.raw("select * from product where product_type='Sweeter'")
    panchus=Product.objects.raw("select * from product where product_type='Panchu'")
    caps=Product.objects.raw("select * from product where product_type='Cap'")
    return render(request,"customer/dashboard.html",{'swals':swals,'sweeters':sweeters,'panchus':panchus,'caps':caps})



def update(request,p_id):
    customer=Customer.objects.get(customer_id=p_id)
    form=CustomerForm(request.POST, instance=customer)
    form.save()
    request.session['username']=request.POST['username']
    users=Customer.objects.get(customer_id=request.session['customer_id'])
    return render(request,"customer/dashboard.html",{'users':[users]})

def logout(request):
    request.session.clear()
    return redirect('/')


