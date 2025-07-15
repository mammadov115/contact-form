from django import forms
from .models import ContactMessage
from django.conf import settings
import requests

class ContactMessageForm(forms.ModelForm):
    email = forms.EmailField(error_messages={'invalid': 'Düzgün bir e-mail ünvanı daxil edin.'})

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'Adınız',
            'email': 'Email ünvanınız',
            'subject': 'Mövzu',
            'message': 'Mesajınız',
        }

    def clean(self):
        captcha_token = self.data.get('g-recaptcha-response')  # reCAPTCHA v2 üçün POST datadan alınır

        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': captcha_token,
        }

        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        response = requests.post(verify_url, data=data)
        result = response.json()

        if not result.get('success'):
            raise forms.ValidationError("Captcha doğrulaması uğursuz oldu. Zəhmət olmasa yenidən cəhd edin.")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Ad ən azı 2 simvoldan ibarət olmalıdır.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) == 0:
            raise forms.ValidationError("Mesaj boş ola bilməz.")
        return message
