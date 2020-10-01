from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import resolve
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
class user_approve_middleware:
    def __init__(self, get_response):
            self.get_response = get_response
      

      
    def __call__(self, request):
      current_url_name = resolve(request.path_info).url_name
      
        
      routes = ['home','login','logout','index']
      if current_url_name not in routes:
      
            if request.user.is_authenticated:
                  pass
            else:

                  messages.info(request, "You need to be logged in to continue...")
                  return HttpResponseRedirect('/')
            

      
      response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

      return response