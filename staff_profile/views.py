from django.shortcuts import render
from about.models import About
from .models import Team, Education, Experience, Certifications, Training, Publication, Projects


# Create your views here.
def index(request):
    tm = Team.objects.all().order_by('display_order')
    exp = Experience.objects.all()
    edu = Education.objects.all()
    cert = Certifications.objects.all()
    train = Training.objects.all()
    publi = Publication.objects.all()
    projects = Projects.objects.all()

    content = {'tm': tm,
               'exp': exp,
               'edu': edu,
               'cert': cert,
               'train': train,
               'publi': publi,
               'projects': projects,
               }
    return render(request, 'staff_profile/index.html', content)
