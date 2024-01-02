from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from .models import UserReg
# Create your views here.
def SignUp(request):
    if request.method=='POST':
        user_name=request.POST.get("username")
        user_mail=request.POST.get("email")
        user_password=request.POST.get("password")
        user_confirmpassword=request.POST.get("conpassword")
        if user_password!=user_confirmpassword:
            return HttpResponse("Invalid Confirm Password")
        else:
            user_credentials=UserReg(user_name=user_name,user_email=user_mail,user_password=user_password)
            user_credentials.save()
            return redirect(Login)
    return render (request,'registration.html')
def Login(request):
    if request.method=='POST':
        user_name=request.POST["username"]
        user_password=request.POST["password"]
        stored_data=UserReg.objects.all()
        for i in stored_data:
            if i.user_name==user_name and i.user_password==user_password:
                return redirect(HomePage)
    return render (request,'login.html')

def HomePage(request):
    if request.method=="POST":
        return redirect(Login)
    return render (request,'home.html') 


