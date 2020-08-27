from django import forms
from .models import Product, Category, Order


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        category = forms.ModelChoiceField(queryset=Category.objects.filter(is_active=True))
        fields = [
            'category',
            'title',
            'detail',
            'img_url'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'rows': '6'}),
        }


class MakeOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        responded = forms.BooleanField(widget=forms.HiddenInput(), required=False)
        fields = [
            'name',
            'phone',
            'email',
            'website',
            'postal_address',
        ]
        help_texts = {
            'name': None
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_address': forms.Textarea(attrs={'rows': '4'}),
        }


class OrderRespondForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            'response',
        ]

        # widgets = {
        #     'response': forms.TextInput(attrs={'class': 'form-control'}),
        # }
