import hashlib
from django.shortcuts import render,redirect
from authenticate import Authentication
from product.models import Product
from buyproduct.models import Buyproduct
from buyproduct.forms import BuyproductForm,DeleteupdateForm
from customer.models import Customer
# Create your views here.
@Authentication.valid_user_where_id
def buypage(request,p_id):
    try:
        product=Product.objects.get(product_id=p_id)
        print(product)
        return render(request, "buypages/buymainpage.html", {'product':product})
    except:
        print("No Data Found")
    return render(request, "buypages/buymainpage.html")

def bill_create(request):
    if request.method == "POST":
        form = BuyproductForm(request.POST)

        if form.is_valid():
            # Get the esewa_id and pin from the form
            esewa_id = form.cleaned_data.get('esewa_id')
            pin = form.cleaned_data.get('pin')

            # Hash the esewa_id and pin using SHA-256
            hashed_esewa_id = hashlib.sha256(esewa_id.encode()).hexdigest()
            hashed_pin = hashlib.sha256(pin.encode()).hexdigest()

            # Save the hashed esewa_id and pin in the Buyproduct model
            buyproduct = form.save(commit=False)
            buyproduct.esewa_id = hashed_esewa_id
            buyproduct.pin = hashed_pin
            buyproduct.save()

            return redirect("/buyproduct/yourproduct")
    else:
        form = BuyproductForm()

    return render(request, "buypages/yourproduct.html", {'form': form})


def yourproduct(request):
    bills = Buyproduct.objects.filter(customer=request.session['customer_id'])
    users = Customer.objects.get(customer_id=request.session['customer_id'])
    return render(request, "buypages/yourproduct.html", {'users': [users], 'bills': bills})


def updatedelete(request,e_id):
    deleteproduct=Buyproduct.objects.get(buyproduct_id=e_id)
    form=DeleteupdateForm(request.POST, instance=deleteproduct)
    form.save()
    return redirect("/buyproduct/yourproduct")