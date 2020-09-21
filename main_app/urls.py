from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('visitor_search/', views.visitor_search_ajax, name="visitor_search"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_user, name="logout")
]   