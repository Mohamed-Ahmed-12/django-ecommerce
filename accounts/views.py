from django.shortcuts import render ,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.


def signup_request(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Sorry, Username is already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST.get('username'),
                    password=request.POST.get('password1')
                    )
                auth.login(request,user)
                print(user ,"<-------------------create an account and login successfully")
                return redirect('store')
        else:
            return render (request,'accounts/signup.html', {'error':'Sorry, Password does not match'})
    else:
        return render(request,'accounts/signup.html')


def login_request(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            print(user , "<-------------------login successfully")
            return redirect('store')         
        else:
            return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'accounts/login.html')


def logout_request(request):
    print(request.user , "<-------------------logout successfully")
    auth.logout(request)
    return redirect('store')
