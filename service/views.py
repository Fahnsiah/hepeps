from .models import Service
from django.shortcuts import render

# Create your views here.
# services function
def index(request):
    service = Service.objects.all()
    return render(request, 'service/index.html', {'service': service})
