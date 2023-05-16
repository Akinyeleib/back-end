from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Article

# Create your views here.

def welcome(request):
    articles = Article.objects.all()

    return render(request, 'welcome.html', {'articles': articles})


def post(request, pk):
    article = Article.objects.get(id=pk)
    
    if request.method == 'GET':
        return render(request, 'blog.html', {'article': article})
    
    elif request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()

        messages.success(request, 'Article updated successfully')
        return redirect('/blog')


def signin(request):

    if request.method == 'POST':
    
        loginID = request.POST["username"].lower()
        password = request.POST["password"]

        user = None
        
        if User.objects.filter(email=loginID).exists():
            user = authenticate(email=loginID, password=password)
            
        elif User.objects.filter(username=loginID).exists():
            user = authenticate(username=loginID, password=password)
        print("User:", user)

        if user is not None:
            login(request, user)
            return redirect('/blog')        
        else:
            messages.error(request, "Invalid Credentials Submitted")


    return render(request, 'login.html')


def signup(request):
    
    if request.method == 'POST':
    
        username = request.POST["username"].lower()
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"].lower()
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        error = False

        if User.objects.filter(username=username).exists():
            error = True
            messages.error(request, 'Username already exists')
        
        if User.objects.filter(email=email).exists():
            error = True
            messages.error(request, 'Username already exists')
        
        if password1 != password2:
            error = True
            messages.error(request, 'Password mismatch')

        if error == False:

            user = User.objects.create_user(username, email, password1)
            user.first_name = firstname
            user.last_name = lastname
            user.set_password(password1)

            user.save()

            messages.success(request, 'User successfully registered')
            return redirect('/blog/login')

    elif request.method == 'GET':
        return  render(request, 'signup.html')

    return  render(request, 'signup.html')


def profile(request):
    
    if request.method == 'POST':
    
        username = request.POST["username"].lower()
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"].lower()
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        error = False

        if User.objects.filter(username=username).exists():
            error = True
            messages.error(request, 'Username already exists')
        
        if User.objects.filter(email=email).exists():
            error = True
            messages.error(request, 'Username already exists')
        
        if password1 != password2:
            error = True
            messages.error(request, 'Password mismatch')

        if error == False:

            user = User.objects.get(username=username)
            
            user.first_name = firstname
            user.last_name = lastname
            user.email = email

            user.set_password(password1)
            user.save()

            messages.success(request, 'Profile successfully updated')
            return redirect('/blog/')

    return  render(request, 'profile.html')


def signout(request):
    logout(request)

    return redirect('/blog')


