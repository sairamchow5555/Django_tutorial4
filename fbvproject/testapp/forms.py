from django import forms
from testapp.models import Employee

class EmplyeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
