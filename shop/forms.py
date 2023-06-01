from .models import *
from django import forms



class ShopFaqForm(forms.ModelForm):

    question_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    userquestion = forms.CharField(label="Текс сообщения:", widget=forms.Textarea(attrs={'max_length': 500, 'class': 'form-control', 'id': 'input-comment', 'placeholder': 'Текст сообщения', 'rows': 10, 'name': 'comment'}))
    # upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = UsersQuestions

        fields = ('userquestion', 'upload')
        widgets = {
            forms.Textarea(attrs={'max_length': 500, 'class': 'form-control', 'id': 'input-comment',
                                  'placeholder': 'Текст сообщения', 'rows': 10, 'name': 'comment'})
        }