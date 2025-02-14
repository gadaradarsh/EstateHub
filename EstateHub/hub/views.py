from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'loginPage.html');
def properties(request):
    return render(request,'admin/managePro.html');
def user(request):
    return render(request,'admin/manageUser.html');
def dashboard(request):
    return render(request,'admin/Dashboard_admin.html');
def review(request):
    return render(request,'admin/review.html');
def inquire(request):
    return render(request,'admin/inquire.html');
def login(request):
    return render(request,'admin/loginPage.html');
def register(request):
    return render(request,'register.html');
def login(request):
    return render(request,'loginPage.html');