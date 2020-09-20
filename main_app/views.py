from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'main_app/index.html')


class DashboardView(View):
    def get(self, request):
        return render(request, 'main_app/dashboard.html')