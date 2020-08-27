from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('order_list>', views.OrderView.as_view(), name='order_list'),
    path('<pk>', views.DetailView.as_view(), name='detail'),
    path('order/<pk>', views.make_order_view, name='order'),
    path('respond/<pk>', views.respond, name='respond'),
    path('order_success/<pk>', views.order_success, name='order_success'),

    path('add', views.AddProductFormView.as_view(), name='add'),
]
