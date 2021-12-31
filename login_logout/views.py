from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserCreationForm, UserRegistrationForm

def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')

            messages.success(request,f'You account has been created!')
            return redirect('login')
    else:
        form= UserRegistrationForm()
    return  render(request,'login_logout/register.html',{"form":form})
def home(request):
    return render(request,'login_logout/home.html')