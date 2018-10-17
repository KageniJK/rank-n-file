from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import PostProjectForm
from .models import Project

# Create your views here.


def index(request):

    return render(request, 'index.html', {'form':upload_form})


@login_required(login_url='/accounts/login/')
def new_project(request):
    user = user.request
    if request.method=='POST':
        upload_form = PostProjectForm(request.POST, request.FILES)
        if upload_form.is_valid():
            project = upload_form.save(commit=False)
            project.user = request.user
            project.save()
    else:
        upload_form=PostProjectForm()

    return render(request, 'new_project.html', {'form':upload_form})