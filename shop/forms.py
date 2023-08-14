from django import forms
from django.db import models
from shop.models import UsersQuestions


class ShopFaqForm(forms.ModelForm):
    question_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    userquestion = forms.CharField(label="Текст сообщения:",
        widget=forms.Textarea(
            attrs={'max_length': 500,
                   'class': 'form-control',
                   'id': 'input-comment',
                   'placeholder': 'Текст сообщения',
                   'rows': 10,
                   'name': 'comment'}))

    class Meta:
        model = UsersQuestions
        fields = ('userquestion', 'upload')
