from django.urls import path
from . import views

urlpatterns = [
    path('<pk>', views.index, name='index'),
    path('<pk>/category', views.category_blog, name='category'),
    path('detail/<int:pk>', views.detail, name='detail'),
]
