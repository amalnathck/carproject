from django.shortcuts import render,redirect
from .models import CustomUser,Car
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,"index.html",{})
def Login(request):
    return render(request,'login page.html')


def cars(request):
    return render(request,'car.html')

def User_register(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        email = request.POST['email']

        username = request.POST['username']
        password = request.POST['pass']

        data = CustomUser.objects.create_user(
                                             phone_number=phone,
                                             username=username,
                                             password=password,
                                             email=email,
                                             user_type = "User"
                                            )

        data.save()
        return render(request,'login page.html')
    else:
        return render(request,'user-register.html')


def Company_register(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        email = request.POST['email']

        username = request.POST['Companyname']
        password = request.POST['pass']

        data = CustomUser.objects.create_user(
            phone_number=phone,
            username=username,
            password=password,
            email=email,
            user_type="company"
        )

        data.save()
        return render(request,'login page.html')
    else:
        return render(request, 'company-register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        data = authenticate(username=username, password=password)
        if data is not None:
            login(request,data)
            if data.user_type == "User":
                return redirect("cars")
            elif data.user_type == "company":
                return redirect("cars1")
        else:
            return render(request,'login page.html', {'message':"invalid credentials"})
    else:
        return render(request,'login page.html')

def userprofile(request):
    data = CustomUser.objects.get(id=request.user.id)
    return render(request, 'profile.html', {'data':data})

def companyprofile(request):
    data = CustomUser.objects.get(id=request.user.id)
    return render(request, 'profile.html', {'data':data})

def cars(request):
    car = Car.objects.all()
    return render(request, 'user/car.html',{'car':car} )

def cars1(request):
    company = CustomUser.objects.get(id=request.user.id)
    car = Car.objects.filter(company_id=company)
    return render(request,'company/car1.html',{'car':car,'Company':company})

def pricing(request):
    return render(request, 'pricing.html', )

def sample(request):
    return render(request, 'sample.html', )

def carbook(request):
    return render(request, 'carbook.html', )


def edit_profile(request):
    User = CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        User.username = request.POST['username']
        User.email = request.POST['email']
        User.phone_number = request.POST['phone']
        User.save()
        return redirect(cars)
    else:
        context = {
            'User':User,
        }
        return render(request,'edit profile.html',context)

def edit_coprofile(request):
    Company = CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        Company.username = request.POST['username']
        Company.email = request.POST['email']
        Company.phone_number = request.POST['phone']
        Company.save()
        return render(request, 'user/car.html', )
    else:
        context = {
            'Company':Company,
        }
        return render(request,'edit-coprofile.html',context)


def Logout(request):
    logout(request)
    return redirect(Login)

def add_car(request):
    company = CustomUser.objects.get(id=request.user.id)
    if request.method=='POST':
        car_name=request.POST['carname']
        price= request.POST['price']
        img1=request.FILES['image']
        model=request.POST['model']
        data=Car.objects.create(company_id=company,
                               car_name=car_name,
                               price=price,
                               image=img1,
                               model=model
                               )

        data.save()
        car=Car.objects.filter(company_id=company)
        return redirect(cars1)
    else:
        car = Car.objects.filter(company_id=company)
        return render(request, 'company/car add.html', {'car': car, 'Company': company})



def edit_car(request,id):
    car = Car.objects.get(id=id)
    if request.method == 'POST':
        car.car_name = request.POST['carname']
        car.price = request.POST['price']
        car.model = request.POST['model']
        if 'image' in request.FILES:
            car.image = request.FILES['image']
        car.save()
        return redirect(cars1)
    else:
        context = {
            'car':car,
        }
        return render(request,'company/editcar.html',context)


def delete_car(request,id):
    car=Car.objects.get(id=id)
    car.delete()
    return redirect(cars1)




