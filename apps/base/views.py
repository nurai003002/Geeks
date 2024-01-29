from django.shortcuts import render
from apps.base import models

# Create your views here.
def index(request):
    title = "Geeks"
    settings = models.Settings.objects.latest('id')
    project = models.Project.objects.all()
    advantages = models.Advantages.objects.all()
    partner = models.Partner.objects.all()
    return render(request, 'base/index.html', locals())

def contact(request):
    settings = models.Settings.objects.latest('id')
    return render(request, 'base/contact.html', locals())
