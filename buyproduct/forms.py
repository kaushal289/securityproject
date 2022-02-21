from django import forms 
from buyproduct.models import Buyproduct

class BuyproductForm(forms.ModelForm):    
    class Meta:
        model = Buyproduct
        fields="__all__"

class DeleteupdateForm(forms.ModelForm):
    class Meta:
        model = Buyproduct
        fields =  ("status",)