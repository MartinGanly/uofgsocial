# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from social.models import Post, Comment, UserProfile, University
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render

# from social.forms import UserForm, UserProfileForm

# Create your views here.
def index(request):
    university_list = University.objects
    context_dict = { 'PageTitle' : 'UofGSocial',
                    'Universities' : university_list}
    response = render(request, 'pages/index.html', context_dict)
    return response

def content(request):
    post_list = Post.objects
    comment_list = Comment.objects
    user_list = UserProfile.objects
    context_dict = { 'PageTitle' : 'Recent Posts',
                    'Users' : user_list,
                    'Posts' : post_list,
                    'Comments' : comment_list}
    reponse = render(request, 'pages/content.html', context_dict)
    return reponse

def editprofile(request):
    post_list = Post.objects
    comment_list = Comment.objects
    user_list = UserProfile.objects
    context_dict = { 'PageTitle' : 'Edit Profile',
                    'Users' : user_list,
                    'Posts' : post_list,
                    'Comments' : comment_list}
    reponse = render(request, 'pages/editprofile.html', context_dict)
    return reponse

def viewprofile(request):
    # request.GET.get('varname','') default = ''
    post_list = Post.objects
    comment_list = Comment.objects
    user_list = UserProfile.objects
    context_dict = { 'PageTitle' : 'View Profile'}
    reponse = render(request, 'pages/viewprofile.html', context_dict)
    return reponse

def login(request):
    context_dict = { 'PageTitle' : 'Login'}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your UofG Social account has been disabled for being inactive for so long")
        else:
            print("Invalid login credentials: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied")

    else:
        response = render(request, 'pages/login.html', context_dict)
        return response

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # This line hashes the password and so is necessary
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'social/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
    reponse = render(request, 'pages/register.html')
    return reponse
