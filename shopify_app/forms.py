from django import forms
from .models import ProductPreferencesModel

class ShopOwnerForm(forms.ModelForm):

    class Meta:
        model = ProductPreferencesModel