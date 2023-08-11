from django.shortcuts import render
from customer.models import Customer
from customer.forms import CustomerForm
from django.shortcuts import redirect
from product.models import Product
from useradmin.models import Useradmin
from product.forms import ProductForm
from buyproduct.models import Buyproduct
from buyproduct.forms import DeleteupdateForm
from useradmin.forms import UseradminForm
import hashlib
from django.contrib import messages
from .forms import UseradminForm

# Create your views here.
def admindash(request):
    if (request.method == "POST"):
        page = int(request.POST['page'])
        if ('prev' in request.POST):
            page = page - 1
        if ('next' in request.POST):
            page = page + 1
        tempOffSet = page - 1
        offset = tempOffSet * 7
        print(offset)
    else:
        offset = 0
        page = 1
    Ctotals=Customer.objects.all().count()
    Ptotals=Product.objects.all().count()
    Ototals=Buyproduct.objects.all().count()
    print(Ctotals)
    customers=Customer.objects.raw("select * from customer limit 7 offset % s", [offset])
    pageItem = len(customers)
    return render(request, "admin/admindash.html", {'Ctotals':Ctotals,'Ototals':Ototals,'Ptotals':Ptotals,'customers': customers, 'page': page, 'pageItem': pageItem})


def adminproduct(request):
    if (request.method == "POST"):
        page = int(request.POST['page'])
        if ('prev' in request.POST):
            page = page - 1
        if ('next' in request.POST):
            page = page + 1
        tempOffSet = page - 1
        offset = tempOffSet * 4
        print(offset)
    else:
        offset = 0
        page = 1

    products=Product.objects.raw('select * from product limit 4 offset % s', [offset])
    pageItem = len(products)
    return render(request,"admin/adminproduct.html",{'products':products, 'page': page, 'pageItem': pageItem})


def customer_delete(request,p_id):
    customer=Customer.objects.get(customer_id=p_id)
    customer.delete()
    return redirect ("/useradmin/admindash")

def billing(request):
    if (request.method == "POST"):
        page = int(request.POST['page'])
        if ('prev' in request.POST):
            page = page - 1
        if ('next' in request.POST):
            page = page + 1
        tempOffSet = page - 1
        offset = tempOffSet * 4
        print(offset)
    else:
        offset = 0
        page = 1

    bills=Buyproduct.objects.raw('select * from buyproduct limit 4 offset % s', [offset])
    pageItem = len(bills)
    return render(request,"admin/billings.html",{'bills':bills, 'page': page, 'pageItem': pageItem})

def updatecomplete(request,e_id):
    completeproduct=Buyproduct.objects.get(buyproduct_id=e_id)
    form=DeleteupdateForm(request.POST, instance=completeproduct)
    form.save()
    return redirect("/useradmin/billing")

def deletebill(request,d_id):
    deletebills=Buyproduct.objects.get(buyproduct_id=d_id)
    deletebills.delete()
    return redirect ("/useradmin/billing")

def userinfo(request):
    if(request.method=="POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page= page-1
        if ('next' in request.POST):
             page=page+1
        tempOffSet = page - 1
        offset=tempOffSet*4
        print(offset)
    else:
        offset=0
        page=1
    users=Useradmin.objects.raw("select * from useradmin limit 4 offset % s",[offset])
    pageItem=len(users)
    return render(request,"admin/viewuser.html",{'users':users,'page':page,'pageItem':pageItem})

def adduser(request):
    if request.method == "POST":
        form = UseradminForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            plain_password = form.cleaned_data.get('password')
            hashed_password = hashlib.sha256(plain_password.encode()).hexdigest()
            user.password = hashed_password
            user.save()

            messages.success(request, "User added successfully.")
            return redirect("/useradmin/userinfo")
    else:
        form = UseradminForm()
    return render(request, "admin/adduser.html", {'form': form})



def edituser(request,p_id):
    try:
       users=Useradmin.objects.get(id=p_id)
       print(users)
       return render(request, "admin/edituser.html", {'users':users})
    except:
       print("No Data Found")
    return redirect("/useradmin/userinfo")


def updateuser(request,p_id):
    user = Useradmin.objects.get(id=p_id)
    form = UseradminForm(request.POST, instance=user)
    if form.is_valid():
        try:
           form. save()
           return redirect("/useradmin/userinfo")
           
        except:
           print("validation failed")
    return render(request, "admin/edituser.html", {'users':user})


def deleteuser(request,p_id):
    try:
       user=Useradmin.objects.get(id=p_id)
       user.delete()
    except:
        print("No data Found")
    return redirect("/useradmin/userinfo")





