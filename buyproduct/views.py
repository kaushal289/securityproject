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
        print(request.POST)
        form = BuyproductForm(request.POST)
        form.save()
        return redirect("/buyproduct/yourproduct")
    else:
        form = BuyproductForm()
    return render(request, "buypages/yourproduct.html")



def yourproduct(request):

    bills=Buyproduct.objects.filter(customer=request.session['customer_id'])
    users=Customer.objects.get(customer_id=request.session['customer_id'])
    return render(request, "buypages/yourproduct.html", {'users':[users],'bills':bills})


def updatedelete(request,e_id):
    deleteproduct=Buyproduct.objects.get(buyproduct_id=e_id)
    form=DeleteupdateForm(request.POST, instance=deleteproduct)
    form.save()
    return redirect("/buyproduct/yourproduct")