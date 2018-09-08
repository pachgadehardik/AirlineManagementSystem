
from django.urls import path

from . import views

urlpatterns =[
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('check/',views.CheckPage,name='check'),
    path('home/',views.Home,name='home'),
    path('book/',views.BookPage,name='book'),
    path('details/',views.Detail,name='detail'),

]