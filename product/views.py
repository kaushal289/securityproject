import os
from django.shortcuts import render,redirect
from product.models import Product
from product.forms import ProductForm

def product_create(request):
    if request.method == "POST":
        print(request.POST)
        form = ProductForm(request.POST,request.FILES)
        form.save()
        return redirect("/useradmin/adminproduct")
    else:
        form = ProductForm()
    return render(request, "admin/addproduct.html", {'form': form})

def deleteproduct(request,p_id):
    product=Product.objects.get(product_id=p_id)
    product.delete()
    return redirect ("/useradmin/adminproduct")
    
def editproduct(request,p_id):
    try:
        product=Product.objects.get(product_id=p_id)
        print(product)
        return render(request, "admin/product_edit.html", {'product':product})
    except:
        print("No Data Found")
    return redirect ("/useradmin/adminproduct")


def productupdate(request,p_id):
    product=Product.objects.get(product_id=p_id)
    if request.method=="POST":
        if len(request.FILES) != 0:
            if len(product.product_image)>0:
                os.remove(product.product_image.path)
            product.product_image=request.FILES['product_image']
    
    print(product)
    form=ProductForm(request.POST, instance=product)
    form.save()
    return redirect ("/useradmin/adminproduct")


    