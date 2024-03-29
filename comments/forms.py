from django import forms


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)
    # parent_id = forms.CharField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label=False, widget=forms.Textarea(
        attrs={
            "class": 'form-control'
        }
    ))
