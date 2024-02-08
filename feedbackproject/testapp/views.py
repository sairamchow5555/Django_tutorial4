from django.shortcuts import render
from testapp.forms import FeedbackForm
# Create your views here.
def feedback_view(request):
    form = FeedbackForm()
    submitted = False
    sname = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print("Form validation success and printing feedback information")
            print("*"*55)
            print("Name:",form.cleaned_data['name'])
            print("Rollno:",form.cleaned_data['rollno'])
            print("Email:",form.cleaned_data['email'])
            print("Password:",form.cleaned_data['password'])
            print("Feedback:",form.cleaned_data['feedback'])
            submitted = True
            sname = form.cleaned_data['name']
        else:
            print('Some filed validation fails.....')
    return render(request,'testapp/feedback.html',{'form':form,'submitted':submitted,'sname':sname})
