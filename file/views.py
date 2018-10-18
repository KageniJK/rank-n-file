from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostProjectForm
from .models import Project

# Create your views here.


def index(request):
    recent = Project.get_recent()
    return render(request, 'index.html', {'recent': recent})


@login_required(login_url='/accounts/login/')
def new_project(request):
    user = request.user
    if request.method == 'POST':
        upload_form = PostProjectForm(request.POST, request.FILES)
        if upload_form.is_valid():
            project = upload_form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('home')
    else:
        upload_form=PostProjectForm()

    return render(request, 'new_project.html', {'form':upload_form, 'user': user})


def one_project(request, id):
    user = request.user
    project = Project.get_by_id(id)

    return render(request, 'project.html', {'user': user, 'project': project})
