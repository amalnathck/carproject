"""
URL configuration for carproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('login',views.Login,name="login"),
    path('user_register',views.User_register, name="user_register"),
    path('company_register', views.Company_register, name="company_register"),
    path('cars',views.cars,name="cars"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('edit_coprofile',views.edit_coprofile,name="edit_coprofile"),
    path('pricing',views.pricing,name="pricing"),
    path('sample',views.sample,name="sample"),
    path('cars1',views.cars1,name="cars1"),
    path('logout',views.Logout,name="logout"),
    path('add_car',views.add_car,name="add_car"),
    path('carbook', views.carbook, name="carbook"),

]
