from django.urls import path
from .import views

urlpatterns =[
    path('', views.SignUp,name="reg"),
    path('login/',views.Login,name="login"),
    path('home/', views.HomePage,name="home"),
]