from django import forms
from .models import MyRecord

class MyRecordForm(forms.ModelForm):
    class Meta:
        model = MyRecord
        fields = ['name', 'age', 'email', 'birth_date']
