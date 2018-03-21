from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime


def home(request):
    
    
    context_dict = {}
    response = render(request, 'rpg/home.html', context=context_dict)
    return response


def about(request):

    context_dict =  {'boldmessage': "about"}
    return render(request, 'rpg/about.html', context=context_dict)
    
def help(request):

    context_dict =  {'boldmessage': "help"}
    return render(request, 'rpg/help.html', context=context_dict)
    
def login(request):

    context_dict =  {'boldmessage': "login"}
    return render(request, 'rpg/login.html', context=context_dict)
    
def register(request):

    context_dict =  {'boldmessage': "register"}
    return render(request, 'rpg/register.html', context=context_dict)
    
def play(request):
    context_dict = {'boldmessage': "play"}
    return render(request, 'rpg/play.html', context=context_dict)
    
def userProfile(request):
    context_dict = {'boldmessage': "userProfile"}
    return render(request, 'rpg/userprofile.html', context=context_dict)
    
def stats(request):
    context_dict = {'boldmessage': "stats"}
    return render(request, 'rpg/stats.html', context=context_dict)



