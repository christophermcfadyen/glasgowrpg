from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.urls import reverse
from rpg.forms import UserForm, UserProfileForm

#home page view
def home(request):
    context_dict = {}
    response = render(request, 'rpg/home.html', context=context_dict)
    return response

#about page view
def about(request):
    context_dict =  {'boldmessage': "about"}
    return render(request, 'rpg/about.html', context=context_dict)

#help page view
def help(request):
    context_dict =  {'boldmessage': "help"}
    return render(request, 'rpg/help.html', context=context_dict)

#login page view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("the account is disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rpg/login.html', {})

#register page view
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'rpg/register.html',
                  {'user_form': user_form,
                   'profile_form':profile_form,
                   'registered':registered})


#Restricted pages.

#stats page view
@login_required
def stats(request):
    #Pass userprofile model to stats.
    from rpg.models import UserProfile

    data = UserProfile.objects.get(user_id=1)

    stu = {"user_id": data}

    return render(request, 'rpg/stats.html', stu)

#userprofile page view
@login_required
def userprofile(request):
    context_dict = {'boldmessage': "userprofile"}
    return render(request, 'rpg/userprofile.html', context=context_dict)


#User should be logged in to play.
#play page view
@login_required
def play(request):
    context_dict = {'boldmessage': "play"}
    return render(request, 'rpg/play.html', context=context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


