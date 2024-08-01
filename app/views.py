from django.shortcuts import render,redirect,get_object_or_404
from .forms import registerForm, LoginForm,AshishForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from.models import Ashish




def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! You have registered successfully.')
            return redirect('login')  
    else:
        form = registerForm()
    return render(request, "blog/register.html", {'form': form})




def login(request):    
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Logged in successfully. Thanks!")
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm() 
    return render(request, "blog/login.html", {'form': form})


def home(request):
    if request.method == 'POST':
        form = AshishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read') 
    else:
        form = AshishForm()
    return render(request, 'blog/home.html', {'form': form})




def read(request):
    all_data = Ashish.objects.all()
    return render(request,"blog/read.html",{'all_data':all_data})


def edit(request,id):
    edit=get_object_or_404(Ashish,pk=id)
    if request.method=='POST':
        form=AshishForm(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form=AshishForm(instance=edit)
    return render(request,"blog/home.html",{'form':form})


def delete(request,id):
    delete = get_object_or_404(Ashish,pk=id)
    if request.method=='POST':
            delete.delete()
            return redirect('read')
    else:
        form=AshishForm(instance=delete)
        return render(request,"blog/delete.html",{'form':form})