from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('logout/',views.logout_page, name='logout_page'),
    path('register/',views.register_page, name='register_page'),
    
    #admin
    path('managePro/',views.properties,name='managePro'),
    path('Dashboard_admin/',views.dashboard,name='Dashboard_admin'),
    path('manageUser/',views.user,name='user_admin'),
    path('review/',views.review,name='review'),
    path('inquire/',views.inquire,name='inquire'),
    
    #buyer
    path('category/',views.category,name='category'),
    path('index/',views.index,name='index'),
    path('inquire_buyer/',views.inquire_buyer,name='inquire_buyer'),
    path('favourite/',views.favourite,name='favourite'),
    path('payment/',views.payment,name='payment'),
    path('review_buyer/',views.review_buyer,name='review_buyer'),

    #seller
    path('Dashboard/',views.Dashboard_seller,name='Dashboard_seller'),
    path('Interestedbuyer/',views.Interestedbuyer,name='Interestedbuyer'),
    path('Managerpro/',views.properties_seller,name='properties_seller'),
    path('respond-inquiries/',views.respond_inquiries,name='respond-inquiries'),
    path('review_seller/',views.review_seller,name='review_seller'),
    path('subscription/',views.subscription,name='subscription'),
    path('transaction/',views.transaction,name='transaction'),
]