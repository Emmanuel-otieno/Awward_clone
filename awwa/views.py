from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    projects = project.objects.all()

    return render(request, 'home.html' , {'projects':projects})

def about(request):
     return render(request, 'about.html',)    