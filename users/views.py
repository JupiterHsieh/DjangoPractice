from pydoc import describe
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User 
from .forms import CustomUserCreationForm


# Create your views here.

# 1. 瀏覽器送出 HTTP request
# 2. Django 依據 URL configuration 分配至對應的 View
# 3. View 進行資料庫操作並回傳 HttpResponse 物件
# 4. 瀏覽器依據 HTTP response 顯示網頁

# 舉例Login的例子來說
# 透過url view render進入login_register.html
# 此時沒有POST method
# def loginPage 還沒被啟動
# 再來 當按下submit 的時候 POST Method 的request被送出 （
# !!! 重點submit 出來的訊息 放在action裡面的url 處理 若action 為空字串 送到前一個介面
# def loginPage 啟動
# https://ithelp.ithome.com.tw/articles/10204953


def loginUser(request):
    page = 'login'
    context = {'page':page }

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user) #create a user session in User's table and add it to browser's cookie 
            return redirect('profiles')
        else:
            messages.error(request,'Username OR password is incorrect')

    return render(request,'users/login_register.html')

def logoutUser(request):
    logout(request) #delete the session
    messages.error(request,"User was log out")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,"User account was created")

            login(request,user)
            return redirect('profiles')
        
        else:
            messages.success(request,"An error has occurred during registration")


    context = {'page':page, 'form':form }
    return render(request, 'users/login_register.html',context)


def profiles(request):
    profiles=Profile.objects.all()
    context = {'profiles':profiles}
    return render(request,'users/profiles.html',context)


def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")

    otherSkills = profile.skill_set.filter(description="")

    context = {'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request,'users/user-profile.html',context)