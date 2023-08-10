from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from customer.forms import CustomerForm
from customer.models import Customer
from product.models import Product
from useradmin.models import Useradmin
from authenticate import Authentication
import hashlib
from django.shortcuts import redirect, render
from customer.forms import CustomerForm
from customer.models import Customer
from product.models import Product
from useradmin.models import Useradmin
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
from .models import FailedLoginAttempt

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            plain_password = form.cleaned_data.get('password')
            hashed_password = hashlib.sha256(plain_password.encode()).hexdigest()
            user.password = hashed_password
            user.save()

            user1 = form.cleaned_data.get('username')
            messages.success(request, "Welcome " + user1 + ", please login here to shop with heavy discount $$$.")
            return redirect("/login")
    else:
        form = CustomerForm()
    return render(request, "auth/registration.html", {'form': form})

MAX_LOGIN_ATTEMPTS = 3
BAN_DURATION_MINUTES = 1

def login_redirect(request):
    if request.method == 'POST':
        username = request.POST["username"]
        plain_password = request.POST["password"]
        hashed_password = hashlib.sha256(plain_password.encode()).hexdigest()

        try:
            user = Useradmin.objects.get(username=username, password=hashed_password)
            if user is not None:
                # Successful login for admin user
                request.session['username'] = request.POST['username']
                request.session['password'] = hashed_password
                return redirect('/useradmin/admindash')
        except Useradmin.DoesNotExist:
            # Check for failed login attempts
            attempt, created = FailedLoginAttempt.objects.get_or_create(username=username)
            now = timezone.now()

            # If there are more than 3 failed attempts and the last attempt was within 1 minute
            if attempt.attempts >= MAX_LOGIN_ATTEMPTS and now - attempt.last_attempt <= timedelta(minutes=BAN_DURATION_MINUTES):
                ban_duration = (now - attempt.last_attempt).seconds // 60 + 1
                messages.error(request, f'Too many failed login attempts. Your account is banned for {ban_duration} minutes.')
                return render(request, "auth/login.html")

            # Validate user credentials
            try:
                customer = Customer.objects.get(username=username, password=hashed_password)
                request.session['username'] = request.POST['username']
                request.session['password'] = hashed_password
                request.session['customer_id'] = customer.customer_id
                
                # Reset failed login attempts
                attempt.attempts = 0
                attempt.last_attempt = None
                attempt.save()

                return redirect('/')
            except Customer.DoesNotExist:
                # Update failed login attempts
                attempt.attempts += 1
                attempt.save()

                if attempt.attempts >= MAX_LOGIN_ATTEMPTS:
                    attempt.last_attempt = now
                    attempt.save()

                messages.error(request, 'Please enter correct username and password')
                return render(request, "auth/login.html")
    else:
        form = CustomerForm()
    return render(request, "auth/login.html", {'form': form})

@Authentication.valid_user
def profile(request):
    users = Customer.objects.get(customer_id=request.session['customer_id'])
    return render(request, "customer/profile.html", {'users': [users]})

def dashboard(request):
    swals = Product.objects.raw("select * from product where product_type='Swal'")
    sweeters = Product.objects.raw("select * from product where product_type='Sweeter'")
    panchus = Product.objects.raw("select * from product where product_type='Panchu'")
    caps = Product.objects.raw("select * from product where product_type='Cap'")
    return render(request, "customer/dashboard.html", {'swals': swals, 'sweeters': sweeters, 'panchus': panchus, 'caps': caps})

def update(request, p_id):
    customer = Customer.objects.get(customer_id=p_id)
    
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            user = form.save(commit=False)
            plain_password = form.cleaned_data.get('password')
            hashed_password = hashlib.sha256(plain_password.encode()).hexdigest()
            user.password = hashed_password
            user.save()

            request.session['username'] = user.username
            users = Customer.objects.get(customer_id=request.session['customer_id'])
            return render(request, "customer/dashboard.html", {'users': [users]})
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, "customer/update_profile.html", {'form': form, 'customer': customer})

def logout(request):
    request.session.clear()
    return redirect('/')
