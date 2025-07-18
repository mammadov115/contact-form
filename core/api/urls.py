from django.urls import path
from .views import ContactFormAPIView

urlpatterns = [
    path('contact/', ContactFormAPIView.as_view(), name='contact-form'),
]
# This URL pattern maps the contact form API view to the 'contact/' endpoint.  