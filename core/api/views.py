from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from django.core.mail import EmailMessage
from django.conf import settings

class ContactFormAPIView(APIView):
    """
    API view for handling contact form submissions.
    """

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            # We will just save the data
            serializer.save()

            full_message = f"""
                Yeni əlaqə mesajı:

                Ad: {serializer.validated_data["name"]}
                Email: {serializer.validated_data["email"]}
                Mövzu: {serializer.validated_data["subject"]}

                Mesaj:
                {serializer.validated_data["message"]}
            """

            # Sending email
            email = EmailMessage(
                subject=f"Yeni əlaqə mesajı: {serializer.validated_data['subject']}",
                body=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[serializer.validated_data["email"]],
            )

            email.send(fail_silently=False)

            return Response({
                "status": "success",
                "message": "Mesajınız uğurla göndərildi!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "status": "error",
            "message": "Göndərilən məlumatlar düzgün deyil.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
