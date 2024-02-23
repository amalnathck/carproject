from django.shortcuts import render,redirect
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,"index.html",{})
def Login(request):
    return render(request,'login page.html')
def user_register(request):
    return render(request,'user-register.html')
def company_register(request):
    return render(request,'company-register.html')

def cars(request):
    return render(request,'car.html')

def User_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['password']

        data = CustomUser.objects.create_user(first_name=first_name,
                                             phone=phone,
                                             username=username,
                                             password=password,
                                             user_type = "User"
                                            )

        data.save()
        return HttpResponse("created")
    else:
        return render(request,'user-register.html')


def Company_register(request):
    if request.method == 'POST':
        company_name = request.POST['first_name']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['password']

        data = CustomUser.objects.create_user(company_name=company_name,
                                              phone=phone,
                                              username=username,
                                              password=password,
                                              user_type="Company"
                                              )

        data.save()
        return HttpResponse("created")
    else:
        return render(request, 'company-register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data = authenticate(username=username, password=password)
        if data is not None:
            login(request,data)
            if data.user_type == "user":
                return redirect("user profile")
            elif data.user_type == "company":
                return redirect("company profile")
            else:
                return HttpResponse("invalid credentials")
    else:
        return render(request,'login page.html')

def userprofile(request):
    data = CustomUser.objects.get(id=request.user.id)
    return render(request, 'profile.html', {'data':data})

def companyprofile(request):
    data = CustomUser.objects.get(id=request.user.id)
    return render(request, 'profile.html', {'data':data})

def cars(request):
    return render(request, 'car.html', )

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(login)
