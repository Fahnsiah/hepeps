from django.shortcuts import render
from .models import BackgroundImages
from staff_profile.models import Team
from service.models import Service
from blog.models import Blog


# Create your views here.
def index(request):
    all_team = Team.objects.filter(is_active=True)
    background_images = BackgroundImages.objects.all()
    service = Service.objects.all()
    content = {
        'all_team': all_team,
        'background_images': background_images,
        'service': service
    }

    return render(request, 'home/index.html', content)
