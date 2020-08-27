from .models import Team
from django.shortcuts import render


def index(request):
    result_list = Team.objects.filter(is_active=True)
    return render(request, 'team/index.html', {'result_list': result_list})


