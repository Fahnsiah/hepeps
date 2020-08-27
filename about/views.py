from django.shortcuts import render
from .models import About, Ourstory, Vision, Mission, Corevalues
#from home.models import HepepsTeam


# Create your views here.
def index(request):
    about_us = About.objects.all().first()
    our_story = Ourstory.objects.all().first()
    our_vision = Vision.objects.all().first()
    our_mission = Mission.objects.all().first()
    our_core_values = Corevalues.objects.all().first()

    content = {
        'about_us': about_us,
        'our_story': our_story,
        'our_vision': our_vision,
        'our_mission': our_mission,
        'our_core_values': our_core_values
       }

    return render(request, 'about/index.html', content)
