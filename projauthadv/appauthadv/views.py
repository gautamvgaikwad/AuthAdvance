from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


# Create your views here.
def homeview(request):
    return render(request,'home.html')


def loginview(request):
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('pw')
        user=authenticate(username=u, password=p)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid credentials')
    temp_nm='login.html'
    return render(request,temp_nm)


def logoutview(request):
    logout(request)
    return redirect('login')


def registerview(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You Registered Successfully!')
            return redirect('login')
    temp_nm='register.html'
    context={'form':form}
    return render(request,temp_nm,context)        


def change_pwview(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password was updated Successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct error')
    else:
        form = PasswordChangeForm(request.user)
    temp_nm='changepw.html'
    context={'form':form}    
    return render(request,temp_nm,context)       
