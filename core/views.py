from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajınız uğurla göndərildi!")

            full_message = f"""
                Yeni əlaqə mesajı:

                Ad: {form.cleaned_data["name"]}
                Email: {form.cleaned_data["email"]}
                Mövzu: {form.cleaned_data["subject"]}

                Mesaj:
                {form.cleaned_data["message"]}
            """

            email = EmailMessage(
                subject=f"Yeni əlaqə mesajı: {form.cleaned_data['subject']}",
                body=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[form.cleaned_data["email"]],
            )
            email.send(fail_silently=False)


            return redirect('home')
        else:
            messages.error(request, "Xəta baş verdi. Zəhmət olmasa, formu düzgün doldurun.")
    else:
        form = ContactMessageForm()
    return render(request, 'contact/contact_form.html', {'form': form, 'RECAPTCHA_SITE_KEY': settings.RECAPTCHA_SITE_KEY})