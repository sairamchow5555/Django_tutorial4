from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    rollno = forms.IntegerField()
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(label='Enter Password',widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re-enter Password',widget=forms.PasswordInput)
    feedback = forms.CharField(widget = forms.Textarea)
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print("Total Form Validation.....")
        total_cleaned_data = super().clean()
        print("Validating RollNo")
        inputrollno = total_cleaned_data['rollno']
        if inputrollno < 0:
            raise forms.ValidationError("RollNo should be > 0")
        print("Validating Name")
        inputname = total_cleaned_data['name']
        if inputname[0].lower() != 's':
            raise forms.ValidationError("Name should starts with s")
        print("Validating email")
        inputemail = total_cleaned_data['email']
        if inputemail[-10:] != '@gmail.com':
            raise forms.ValidationError("Email extenion should be @gmail.com")
        print("Validating Password")
        pwd = total_cleaned_data['password']
        rpwd = total_cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError("Both passwords must be same")
        print("Validating bot_handler")
        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError("Request from Bots are not allowed")
