from django import forms


class NumberBuySoftwareLicense(forms.Form):
    quantity_license = forms.IntegerField(min_value=1, max_value=1000)
