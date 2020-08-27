from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ListView.as_view(), name='list'),
    path('message', views.contact_message_form_view, name='message'),
    path('success', views.success, name='success'),
    path('respond/<int:mid>', views.respond, name='respond'),
    # path('message', views.ContactMessageFormView.as_view(), name='message'),
]
