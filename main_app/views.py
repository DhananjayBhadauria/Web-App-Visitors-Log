from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'main_app/index.html')


class DashboardView(View):
    def get(self, request):
        return render(request, 'main_app/dashboard.html')

def visitor_search_ajax(request):
    data= request.POST.get('data').strip()
    visitors = Visitor.objects.filter(Q(full_Name__icontains=data, Organization=request.user.profile)|
    Q(contact_Number__icontains=data, Organization=request.user.profile)
    )
    return render(request, 'main_app/visitors_search.html', {'visitors':visitors})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            g_user = User.objects.get(email= username) # checkng whether user registered or not 
            username = g_user.username
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Username or Password incorrect!')
                return render(request, 'main_app/index.html')
        except:
            messages.error(request, 'No user found with this mail!')
            return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, "User logged out!")
    return redirect('home')