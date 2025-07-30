from django.shortcuts import render
from django.http import HttpResponse
from .models import Organization, Division, Conference, Team, Bowl, Rivalry
# Create your views here.


def index(request):
    organizations = Organization.objects.all()
    context = {
        'organizations': organizations,
    }
    return render(request, 'CFB/index.html', context)