from django.shortcuts import render,redirect
from django .http import HttpResponse
from.models import Project
from .forms import NewProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    projects = project.objects.all()

    return render(request, 'home.html' , {'projects':projects})



@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'add-project.html', {"form": form})     
