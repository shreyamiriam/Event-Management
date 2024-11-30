from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def user(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        e_mail=request.POST.get('email')
        p_assword=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')

        if p_assword==confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=e_mail).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else:
                user_reg=User.objects.create_user(username=user_name,email=e_mail,password=p_assword)
                user_reg.save()
                messages.info(request,"Successfully created")
                # return redirect('/')
                return redirect('register')
        else:
            messages.info(request,"Password doesn't match")
            return redirect('register')
    
    return render(request,'reg.html')

def login(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        user=auth.authenticate(username=user_name,password=pass_word)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Login Success")
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('register')
        
        
    return render(request,'log.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
