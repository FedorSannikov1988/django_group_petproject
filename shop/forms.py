from shop.models import Feedback
from django import forms


class ShopFaqForm(forms.Form):
    question = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Тескт сообщения'}))
    field = ["question"]

