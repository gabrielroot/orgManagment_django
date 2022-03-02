from django.http import HttpResponse
from django.shortcuts import render 
from django.views import View

class UserView(View):
    def get(self, request):
        return render(request, 'core/users/index.html')