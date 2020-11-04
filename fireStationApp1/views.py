from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from fireStationApp1.EmailBackend import EmailBackend


def homePage(request):
    return HttpResponse("Helloworld")

def showDemoPage(request):
    return render(request,"hello.html")

def showLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!= "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!= None:
            login(request, user)
            return HttpResponseRedirect("/admin_home")
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def getUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email)
    else:
        return HttpResponse("Please Login first")

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")