from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect, render
from django.contrib import messages
from .forms import LoginForm, UserEditForm, UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def loginpage(request):
    if request.method == "POST":
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            
            #if there is any user with this password then we will user object, other wise none. 
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = LoginForm()
    return render(request, 'login.html', {'form':fm})


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulation you have been registered! Now you can login')
            return HttpResponseRedirect('/')
    else:
        form = UserRegistrationForm()
    
    return render(request,'signup.html',{'form':form})


def profile(request):
    if request.user.is_authenticated:    
        userdetail = User.objects.get(pk=request.user.id)
        # print(request.user.id) will get user id
        # print(userdetail.email) will get email id
        return render(request,'profile.html',{'user':userdetail})
    else:
        return HttpResponseRedirect('/')


#logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/')

#edit
def editprofile(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = User.objects.get(pk=id)
            form = UserEditForm(request.POST, instance=pi)
            if form.is_valid:
                form.save()
                messages.success(request,'Details Updated succesfully')
        else:
            pi = User.objects.get(pk=id)
            form = UserEditForm(instance=pi)

        return render(request, 'edit.html', {'form': form})
    return HttpResponseRedirect('/')