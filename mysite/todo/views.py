from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Project


def index(request):
    latest_project_list = Project.objects.order_by("-pub_date")[:5]
    context = {
        "latest_project_list": latest_project_list,
    }
    return render(request, "todo/index.html", context)


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "todo/detail.html", {"project": project})


def results(request, project_id):
    response = "Your're looking at the results of project %s."
    return HttpResponse(response % project_id)


def edit(request, project_id):
    return HttpResponse("You're editing project %s." % project_id)
