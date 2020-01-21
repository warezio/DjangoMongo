from django import forms

from .models import mydb

class mydbForm(forms.ModelForm):

    class Meta:
        model = mydb
        fields = ('field', 'type', 'default', 'value')
