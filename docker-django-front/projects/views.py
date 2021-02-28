from django.shortcuts import render
from projects.models import Project
import requests

def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    response = requests.get('http://localhost:80/api/v1/resources/books/all')
    all_books = response.json()
    context = {"project": project, "books": all_books}
    return render(request, "project_detail.html", context)


