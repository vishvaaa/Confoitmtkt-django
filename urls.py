from django.urls import path
from . import views



urlpatterns = [
    path('index/', views.index),
    path('home/', views.home),
    path('about/', views.about),
    path('services/', views.services),
    path('helpline/', views.helpline),
    path('contact/', views.contact),
    path('signin/', views.signin),
    path('register/',views.register),

    # path('box1home/',views.box1),
    # path('userDetailsSave',views.userDetailsAdd,name='userDetailsSave')

]