from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm
from django.http import HttpResponse
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime


def index(request):
    
    request.session.set_test_cookie()
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
    
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    response = render(request, 'rango/index.html', context=context_dict)
    return response


def about(request):
    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED!")
        request.session.delete_test_cookie()
    context_dict =  {'boldmessage': "Chris"}
    return render(request, 'rango/about.html', context=context_dict)
    

    
# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val
    
    
def visitor_cookie_handler(request, response):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                                'last_visit',
                                                str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                            '%Y-%m-%d %H:%M:%S')
                                            # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        #update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        # set the last visit cookie
        request.session['last_visit'] = last_visit_cookie
        # Update/set the visits cookie
    request.session['visits'] = visits



