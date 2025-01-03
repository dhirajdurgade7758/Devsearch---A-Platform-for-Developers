from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, EditProfile, SkillForm, MessageForm
from django.db.models import Q
from .utils import searchProfiles, paginateProfiles

# Create your views here.
def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request,profiles,6)
    context = {'profiles':profiles, 'search_query': search_query, "custom_range":custom_range}
    return render(request,"users/profiles.html",context)

def user_profile(request,pk):
    profile = Profile.objects.get(id = pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description = "")

    context = {"profile":profile, "topSkills":topSkills, "otherSkills": otherSkills}
    return render(request,"users/user-profile.html", context)

def login_page(request):
    page = "login"
    if request.user.is_authenticated:
        print(request.user)
        return redirect('profiles')
    if request.method == "POST":
        username =  request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)

        except:
            messages.error(request,'user does not exists!')

        user = authenticate(request, username=username , password= password)

        if user is not None:
            login(request,user)
            messages.success(request, "user login sucessfully")
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request,"username or the password is incorrect")
    
    context = {'page':page}
    return render(request, 'users/login_register.html', context)

def logout_page(request):
    logout(request)
    messages.info(request, "user has logout sucessfully")
    return redirect('profiles')


def register_page(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            messages.success(request, "User was created successfully!")
            return redirect('edit_account')
        else:
            messages.error(request, "An error occurred during registration")

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

@login_required(login_url="login")
def user_account(request):
    profile = request.user.profile
    Skills = profile.skill_set.all()
    projects = profile.projects_set.all()
    context = {'profile':profile, 'skills':Skills, 'projects': projects}
    return render(request,'users/account.html', context)

@login_required(login_url="login")
def edit_account(request):
    profile = request.user.profile

    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    form = EditProfile(instance=profile)
    context = {"form":form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url="login")
def add_skill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "skill was created sucessfully")
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/skill_form.html',context)

@login_required(login_url="login")
def update_skill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance = skill)
        if form.is_valid():
            form.save()
            messages.success(request, "skill was updated sucessfully")
            return redirect('account')

    context ={'form':form}
    return render(request, 'users/skill_form.html',context)

@login_required(login_url="login")
def delete_skill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "skill was deleted sucessfully")
        return redirect('account')
    context = {'object':skill}
    return render(request, 'delete-template.html',context)

@login_required(login_url="login")
def inbox(request):
    messagesRequest = request.user.profile.messages.all()
    unReadCount = request.user.profile.messages.filter(is_read=False).count()
    context = {"messagesRequest":messagesRequest, "unReadCount":unReadCount}
    return render(request, 'users/inbox.html', context)

@login_required(login_url="login")
def view_message(request,pk):
    messageRequest = request.user.profile.messages.get(id = pk)
    if messageRequest.is_read == False:
        messageRequest.is_read = True
        messageRequest.save()
    context = {"messageRequest":messageRequest}
    return render(request, 'users/message.html',context)

def create_message(request,pk):
    recipient = Profile.objects.get(id = pk)
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.sender = request.user.profile
                message.name = request.user.profile.name
                message.email = request.user.profile.email
            message.recipient = recipient
            message.save()
            messages.success(request, "your message was successfully sent!")
            return redirect('user_profile',recipient.id)
        
    context = {"form":form, 'recipient':recipient}
    return render(request, "users/message_form.html", context)