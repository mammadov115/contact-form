from rest_framework import serializers
from ..models import ContactMessage

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        extra_kwargs = {
            'name': {'required': True, 'min_length': 3, 'error_messages': {'required': 'Enter your name.', 'min_length': 'Name must be at least 3 characters long.'}},
            'email': {'required': True, 'error_messages': {'required': 'Enter your email', 'invalid': 'Enter a valid email address.'}},
            'subject': {'required': True, 'error_messages': {'required': 'Enter the subject of your message.'}},
            'message': {'required': True, 'error_messages': {'required': 'Enter your message.', 'blank': 'Message cannot be blank.'}},
        }

    