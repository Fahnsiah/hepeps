from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic import View
from util.views import email_response
from .models import Product, Order
from .form import AddProductForm, MakeOrderForm, OrderRespondForm


class IndexView(generic.ListView):
    template_name = 'product/index.html'
    context_object_name = 'result_list'

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class OrderView(generic.ListView):
    template_name = 'product/order_list.html'
    context_object_name = 'result_list'

    def get_queryset(self):
        return Order.objects.all().order_by('-created_on')


class DetailView(generic.DetailView):
    model = Product
    context_object_name = 'result'
    template_name = 'product/detail.html'


# class AddProductForm(PermissionRequiredMixin, generic.ListView):
#     permission_required = 'cause.can.view.product'

class AddProductFormView(PermissionRequiredMixin, View):
    permission_required = 'product.can.add.product'
    form_class = AddProductForm
    template_name = 'product/add.html'

    def get(self, request):
        form = self.form_class(None)
        content = {
            'form': form
        }
        return render(request, self.template_name, content)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = self.form_class(None)
            content = {
                'form': form,
                'success': 'Product added successfully.'
            }
            return render(request, self.template_name, content)
        else:
            content = {
                'form': form,
                'error': 'Error: Invalid form.'
            }
            return render(request, self.template_name, content)


# @permission_required('product.can.add.product')
def make_order_view(request, pk):
    form_class = MakeOrderForm
    template_name = 'product/order.html'
    product = Product.objects.get(id=pk)
    if request.method == 'GET':
        form = form_class(None)
        content = {
            'form': form,
            'product': product
        }
        return render(request, template_name, content)

    else:
        form = form_class(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()

            return redirect('product:order_success', pk=pk)
        else:
            content = {
                'form': form,
                'product': product,
                'error': 'Error: Invalid form.'
            }
            return render(request, template_name, content)


@permission_required('order.can.add.order')
def respond(request, pk):
    form_class = OrderRespondForm
    template_name = 'product/respond.html'
    order = Order.objects.get(id=pk)
    if request.method == 'GET':
        form = form_class(None)
        content = {
            'form': form,
            'order': order
        }
        return render(request, template_name, content)

    else:
        form = form_class(request.POST)
        if form.is_valid():
            order = Order.objects.get(id=pk)
            if order.response:
                order.response = request.POST.get('response') + ' \n\nPrevious Message\n' + order.response
            else:
                order.response = request.POST.get('response')
            order.responded = True
            order.save()

            # send email
            message = order.response
            recipient = [order.email]
            email_response(message=message, recipients=recipient)
            return redirect('product:order_list')
        else:
            content = {
                'form': form,
                'order': order,
                'error': 'Error: Invalid form.'
            }
            return render(request, template_name, content)


def order_success(request, pk):
    template_name = 'product/order_success.html'
    content = {
        'success': 'Thank you for making an order. An email has been sent to the email'
                   ' address you provided detailing how your order will be processed.'
    }
    return render(request, template_name, content)




