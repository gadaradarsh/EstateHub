from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Views for rendering pages
def home(request):
    return render(request, 'login.html')

def properties(request):
    return render(request, 'admin/managePro.html')

def user(request):
    return render(request, 'admin/manageUser.html')

def dashboard(request):
    return render(request, 'admin/Dashboard_admin.html')

def review(request):
    return render(request, 'admin/review.html')

def inquire(request):
    return render(request, 'admin/inquire.html')

# User login
def login_page(request):
    if request.method == "POST":
        User_Name = request.POST.get('Uname')  # Matches HTML input name
        Password = request.POST.get('password')

        # Authenticate user
        user_new = authenticate(username=User_Name, password=Password)
        if user_new:
            login(request, user_new)  # Bind user to session
            return redirect('dashboard_admin')  # Redirect to a dashboard or appropriate page
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login_page')  # Stay on the same page if credentials are invalid

    return render(request, 'login.html')


# User logout
def logout_page(request):
    logout(request)
    return redirect('login_page')  # Replace with correct URL name

# User registration
def register_page(request):
    if request.method == "POST":
        First_Name = request.POST.get('Fname')
        Last_Name = request.POST.get('Lname')
        User_Name = request.POST.get('Uname')
        Email = request.POST.get('email')
        Password = request.POST.get('password')

        # Check if all fields are provided
        if not all([First_Name, Last_Name, User_Name, Email, Password]):
            messages.error(request, "All fields are required.")
            return redirect('register_page')

        # Check if username already exists
        if User.objects.filter(username=User_Name).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register_page')

        try:
            # Create user object
            user = User.objects.create_user(
                username=User_Name,
                email=Email,
                password=Password,
                first_name=First_Name,
                last_name=Last_Name
            )
            messages.success(request, 'Account Created Successfully.')
            return redirect('login_page')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('register_page')

    return render(request, 'register.html')
