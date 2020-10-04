from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('visitor_search/', views.visitor_search_ajax, name="visitor_search"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_user, name="logout"),
    
    path('visitor_details/<int:pk>/', VisitorDetail.as_view(), name="visitor_details"),
    path('visitor_details_updates/', views.visitor_detail_update_form_handle, name="visitor_details_update"),
    path('profile/update/', OrganizationUpdateView.as_view(), name="org_update_view"),
    path('visit_edit_ajax/', views.ajax_edit_visit, name="ajax_edit_visit"),
    path('edit_visit_view', EditVisitView.as_view(), name="editVisitView"),
    path('visitors_by_date/', VisitorsByDateView.as_view(), name="visitor_by_date"),
    path('ajax_visitor_by_date_call/', views.ajax_visitors_by_date, name="ajax_vis_by_date"),
]   