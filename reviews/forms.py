from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label='Name', max_length=15, required=True)
#     review = forms.TextInput()
#     rating = forms.IntegerField(required=True)

class ReviewForm(forms.ModelForm):
    name = forms.CharField(
        error_messages={'required': 'Please let us know what to call you!'}
    )
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ("review",)
        labels = {
            "name": "Your name",
            "review": 'Your feedback',
        }

