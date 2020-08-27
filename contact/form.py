from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'subject',
            'message'
        ]

    # def Firstname(self):
    #     data = self.cleaned_data.get('first_name')
    #     if '' in data:
    #         raise forms.ValidationError('Please enter first name')
    #     return data

    def clean(self):
        cleaned_data = super().clean()
        data = self.cleaned_data.get('first_name')
        if data == '':
            raise forms.ValidationError('Please enter first name')
        return cleaned_data


class ContactResponseForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = [
            'response',
        ]
