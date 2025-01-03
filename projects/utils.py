from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProjects(request, projectlist, results):
    page = request.GET.get('page')
    if page == None:
        page = 1
    paginator = Paginator(projectlist, results)

    try:
        projectlist = paginator.page(page)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.num_pages
        projectlist =paginator.page(page)

    left_index = (int(page)-4)
    if left_index < 1:
        left_index = 1
    
    right_index =  (int(page) + 5)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, projectlist

def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    tags = Tag.objects.filter(name__icontains = search_query)

    projectlist = Projects.objects.distinct().filter(
        Q(title__icontains = search_query)|
        Q(description__icontains = search_query)|
        Q(owner__name__icontains = search_query)|
        Q(tag__in = tags)
    )
    return search_query, projectlist