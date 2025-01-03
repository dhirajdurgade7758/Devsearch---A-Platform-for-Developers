from django.shortcuts import render,redirect
from .models import *
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .utils import searchProjects, paginateProjects
# Create your views here.
  
def projects(request):
    search_query, projectlist = searchProjects(request)
    results = 6
    custom_range, projectlist = paginateProjects(request, projectlist,results)
    context = {'projects':projectlist, 'search_query': search_query, 'custom_range': custom_range}
    return render(request,"projects/projects.html",context)

def project(request,pk):
    projectobj = Projects.objects.get(id = pk)

    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid:
           review = form.save(commit=False)
           review.owner =  request.user.profile 
           review.project = projectobj
           review.save()
           projectobj.getVoteCount
           messages.success(request, 'your review was sucessfully submitted!')
           return redirect('project', pk=projectobj.id)
    return render(request,"projects/single_project.html",{"project":projectobj, "form":form}) 

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile 
    form = ProjectForm()
    if request.method == 'POST':
        newtags  = request.POST.get('newtags').replace(',', ' ').split()
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid:
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tag.add(tag)
            return redirect('projects')

    context ={'form':form}
    return render(request,"projects/frm.html",context)

@login_required(login_url='login/')
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.projects_set.get(id = pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        newtags  = request.POST.get('newtags').replace(',', ' ').split()
        print("DATA: ", newtags) 
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tag.add(tag)
            return redirect('projects')

    context ={'form':form, 'project':project}
    return render(request,"projects/frm.html",context)

@login_required(login_url='login/')
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.projects_set.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect("account")

    context = {"object":project}
    return render(request, "delete-template.html",context)

