from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
# Create your views here.
class users(View):
    def get(self , request):
        return render(request , "users/index.html")

    def post(self , request):
        if "signup" in request.POST:
            if ("name" and "pass" and 'email' in request.POST):
                name = request.POST['name']
                password = request.POST['pass']
                email = request.POST['email']
                u = User.objects.create_user(
                    username = name,
                    password = password , 
                    email = email
                )
                u.save()
                return redirect('/')
            else:
                return HttpResponse("full the fields")
        elif 'signin' in request.POST:
            if( 'username' in request.POST and
                "pass" in request.POST 
            ):
                username = request.POST['username']
                password = request.POST['pass']
                u = authenticate(
                    request ,
                    username = username,
                    password = password,
                )
                if u:
                    login(request , u)
                    return redirect("/")
                else:
                    return HttpResponse("your name or password is wrong ")
            else:
                return HttpResponse("full the fields")

class logoutt(View):
    def get(self , request):
        logout(request)
        return redirect("/users/u")