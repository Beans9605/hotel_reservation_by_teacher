from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import CustomUser
# Create your views here.

def sign_up(request) :
    if request.method == "POST" :
        username = request.POST['username']
        phone = str(request.POST['phone'])
        email = request.POST['email']
        password = request.POST['password']

        if CustomUser.objects.filter(username=username).distinct() :
            context = {"err" : "User is already exist"}
            return render(request, 'user/sign_up.html', context)
        
        user = CustomUser(
            username = username,
            email = email,
            phone_number = phone
        )
        user.set_password(password)

        user.save()

        request.session['user'] = user.username

        return redirect("home")
    return render(request, "user/sign_up.html")

def sign_in(request) :
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        try :
            user = CustomUser.objects.get(username=username)
        except :
            context = {"err" : "Does not exist id"}
            return render(request, 'user/sign_in.html', context)

        if check_password(password, user.password) :
            request.session['user'] = user.username
            return redirect('home')
        else :
            context = {"err" : "Does not match password"}
            return render(request, 'user/sign_in.html', context)
    return render(request, 'user/sign_in.html')

def logout(request) :
    if request.session.get('user', False) :
        request.session.modified = True
        del request.session['user']
        return redirect('home')
    else :
        return redirect('home')


def mypage(request):
    return render(request, 'mypage/mypage.html')