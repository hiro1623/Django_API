from django import forms

from .models import PostData

"""
POST_CHOICE = (
    ('SOS','SOS'),
    ('災害情報','災害情報'),
    ('落し物','落し物'),
    ('人探し','人探し'),
    ('その他','その他'),
)

class PostingForm(forms.Form):

        message = forms.CharField(
            label='メッセージ',
            max_length=200,
            required=True,
            widget=forms.Textarea(
                attrs={'rows':5,'placeholder':'What is on your mind?'}
            )
        )
        purpose = forms.ChoiceField(
            label='投稿の種類',
            widget=forms.Select,
            choices = POST_CHOICE,
            required=True,
        )
        pic = forms.ImageField(
            label='写真',
            required=False,
        ) 
"""        
