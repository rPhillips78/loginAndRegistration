from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    if 'logged_in' not in request.session:
        request.session['logged_in'] = False
    print(request.session['logged_in'])
    return render(request, 'login_app/index.html')

def register(request):
    errors = User.objects.register_func(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val, extra_tags='register_tag')
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email_add'], password=hashed_pw.decode(), confirm_pw=request.POST['password_confirm'])

        request.session['logged_in'] = True
        request.session['user_id'] = new_user.id
        print(request.session['logged_in'])
        return redirect('/success')


def login(request):
    errors = User.objects.login_func(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val, extra_tags='login_tag')
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['user_email'])
        try:
            if bcrypt.checkpw(request.POST['user_password'].encode(), user.password.encode()):
                request.session['logged_in'] = True
                print(request.session['logged_in'])
                return redirect('/success')
                
        except:
            print("Cannot find user!")
            request.session['logged_in'] = False
            print(request.session['logged_in'])
            return redirect('/')

def login_display(request):
    if request.session['logged_in'] == True:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user
        }
        print(request.session['logged_in'])
        return render(request, 'login_app/login.html', context)
    else:
        return redirect('/')    


def welcome(request):
    if request.session['logged_in'] == True:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user
        }
        print(request.session['logged_in'])
        return render(request, 'login_app/login.html', context)
    else:
        return redirect('/') 

def logout(request):
    request.session.clear()
    request.session['logged_in'] = False
    print(request.session['logged_in'])
    return redirect('/')
