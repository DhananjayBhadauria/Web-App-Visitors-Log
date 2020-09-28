from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.db.models import Q, Max
from .forms import *
from django.utils import timezone
from django.urls import reverse
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'main_app/index.html')


class DashboardView(View):
    
    def get(self, request):
        form = VisitorForm()
        context = {
            'form':form
        }
        return render(request, 'main_app/dashboard.html', context)
    
    def post(self, request):
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.instance.Organization = request.user.profile
            form.instance.date_Registered = timezone.now()
            new_visitor = form.save()
            messages.success(request,'Added successfully!')
            return HttpResponseRedirect(reverse('visitor_details', kwargs={'pk':new_visitor.id}))
        else:
            context={
                'form':form
            }
            return render(request, 'main_app/dashboard.html', context)
        return render(request, 'main_app/dashboard.html', )


def visitor_search_ajax(request):
    data= request.POST.get('data').strip()
    
    visitors = Visitor.objects.filter(Q(full_Name__icontains=data, Organization=request.user.profile)|
    Q(contact_Number__icontains=data, Organization=request.user.profile)
    )
    if len(data) <2:
        visitors = []

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

class VisitorDetail(View):
    form = VisitorForm()
    
    
    def get(self, request, pk):
        visitor = Visitor.objects.get(id=pk, Organization= request.user.profile)
        total_visits = visitor.visits.all().order_by('-visit_Number')
        add_visit_form = VisitAddForm(initial={'visitor':visitor.full_Name,'visit_Date':timezone.now() })
        context = {
            "form":self.form,
            'visitor':visitor,
            'total_visits': total_visits,
            'add_visit_form':add_visit_form
        }
        return render(request, 'main_app/visitor_detail.html', context)

    def post(self, request, pk):
        visitor = Visitor.objects.get(id=pk, Organization= request.user.profile)
        total_visits = visitor.visits.all()
        add_visit_form = VisitAddForm(request.POST)
        
        if add_visit_form.is_valid():
            add_visit_form.instance.Organization = request.user.profile
            add_visit_form.instance.visitor = visitor
            
            saved_visit = add_visit_form.save(commit=False)
            visitor.last_visit = saved_visit.visit_Date #updating visitors last visit value
            visitor.save()
            # starting logic for visit no.
            visits = VisitDetails.objects.filter(visitor= saved_visit.visitor)
            max_visit_no =  visits.aggregate(Max('visit_Number'))
            
            if max_visit_no['visit_Number__max'] is None:
                saved_visit.visit_Number = 1
                saved_visit.save() 
            else:
                saved_visit.visit_Number = max_visit_no['visit_Number__max']+1
                messages.success(request, 'Created successfully!')
                saved_visit.save()
                
                
            # ending logic for visit no.
            return HttpResponseRedirect(reverse('visitor_details', kwargs={'pk':visitor.id}))
        else:
            add_visit_form = add_visit_form
            print(add_visit_form.errors)
        context = {
            "form":self.form,
            'visitor':visitor,
            'total_visits': total_visits,
            'add_visit_form':add_visit_form
        }
        return render(request, 'main_app/visitor_detail.html', context)



class OrganizationUpdateView(View):
    

    def get(self, request):
        current_user = UserProfile.objects.get(user = request.user)
        org_update_form = OrganizationUpdateForm(instance=current_user)
        context = {
            'org_update_form':org_update_form
        }
        return render(request, 'main_app/organization_update.html', context)

    def post(self, request):
        current_user = UserProfile.objects.get(user = request.user)
        org_update_form = OrganizationUpdateForm(request.POST, request.FILES ,instance=current_user)
        if org_update_form.is_valid():
            org_update_form.save()
            messages.success(request, 'Profile updated successfully!')
            org_update_form = OrganizationUpdateForm(instance=current_user)
            
        else:
            org_update_form= org_update_form

        context={
            'org_update_form':org_update_form
        }
        return render(request, 'main_app/organization_update.html', context)

