from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostProjectForm, VoteForm
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
    if request.method == 'POST':
        vote_form = VoteForm(request.POST, request.FILES)
        if vote_form.is_valid():
            rating = vote_form.save(commit=False)
            rating.user = request.user
            rating.project = project
            rating.save()
            return redirect('project', project.id)
    else:
        vote_form=VoteForm()
    return render(request, 'project.html', {'user': user, 'project': project, 'vote_form':vote_form})
