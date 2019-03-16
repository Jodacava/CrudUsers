from django import forms
from .models import Users

class userform(forms.ModelForm):
    class Meta:
        model = Users
        fields = {
            'name',
            'password',
            'uclass',
        }