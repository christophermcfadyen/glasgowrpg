from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime


def index(request):
    
    
    context_dict = {}
    response = render(request, 'rpg/home.html', context=context_dict)
    return response


def about(request):

    context_dict =  {'boldmessage': "Chris"}
    return render(request, 'rpg/about.html', context=context_dict)
    



