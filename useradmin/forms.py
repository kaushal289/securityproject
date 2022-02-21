from django import forms
from useradmin.models import Useradmin

class UseradminForm(forms.ModelForm):
    
    class Meta:
        model = Useradmin
        fields = ('__all__')