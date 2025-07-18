import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.core import mail
from pytest_mock import mocker

# DRF test client  
client = APIClient()


@pytest.mark.django_db
class TestContactsFormAPI:
    def test_valid_contact_submission_returns_201(self):
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "subject": "Test subject",
            "message": "This is a test message."
        }
        response = client.post("/api/contact/", data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["email"] == "john@example.com"
        assert len(mail.outbox) == 1


    def test_missing_fields_returns_400(self, mocker):
        data = {
            "name": "",
            "email": "notanemail",
            "subject": "",
            "message": ""
        }
        mock_send = mocker.patch("django.core.mail.EmailMessage.send")

        response = client.post("/api/contact/", data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "name" in response.data
        assert "email" in response.data 
        assert "subject" in response.data
        assert "message" in response.data
        mock_send.assert_not_called()

    def test_throttling_on_contact_form(self):
        data = {
            "name": "Test",
            "email": "test@example.com",
            "subject": "Hi",
            "message": "Testing throttling"
        }

        for _ in range(10):
            response = client.post("/api/contact/", data, format='json')
            assert response.status_code in [201, 429]  # 201 for success, 429 for throttling    
            
        # Check if the last request is throttled
        response = client.post("/api/contact/", data, format='json')
        print(response.status_code)
        assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS