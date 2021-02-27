from django.shortcuts import render
from projects.models import Project
import requests

def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    response = requests.get('https://ghibliapi.herokuapp.com/films')
    vehicles = response.json()
    movie1 = vehicles[0]
    context = {"project": project, "details": movie1}
    return render(request, "project_detail.html", context)


def get_ip(request):
    print("=====================================================YYYYYYYY================")
    response = requests.get('https://ghibliapi.herokuapp.com/vehicles')
    return response
