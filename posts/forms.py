from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a title...'
        }))
    content = forms.CharField(widget=PagedownWidget(show_preview=False,
        attrs={
            'class': 'form-control',
            'style': 'margin-left: -25%;',
            'placeholder': 'Contents goes here...'
        }))

    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={
            'class': 'form-control-file',

        }
    ))

    draft = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'style': 'margin-left: 1%;',
        }
    ))

    publish = forms.DateField(required=False, initial="2018-06-21", widget=forms.SelectDateWidget(
        attrs={
            # 'class': 'form-control ',

        }
    ),)

    class Meta:
        model = Post

        fields = [
            'title',
            'content',
            'image',
            'draft',
            'publish',
        ]

