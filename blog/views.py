from django.shortcuts import render,redirect

def home(request):
    return render(request,'blog/home.html')


