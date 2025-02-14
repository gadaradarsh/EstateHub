from django.urls import path
from . import views 

urlpatterns =[
    path('',views.home,name='home'),
    path('managePro.html',views.properties,name='manage_properties'),
    path('Dashboard_admin.html',views.dashboard,name='dashboard_admin'),
    path('manageUser.html',views.user,name='user_admin'),
    path('review.html',views.review,name='review'),
    path('inquire.html',views.inquire,name='inquiry'),
    path('register.html',views.register,name='register'),
    path('loginPage.html',views.login,name='login'),
]