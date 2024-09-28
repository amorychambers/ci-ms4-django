from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

def contact(request):
    """
    View to return and handle contact form,
    with about us info
    """
    form = ContactForm()

    if request.method == "POST":
        """
        Send email to our inbox for customer contact
        """

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')

        subject = render_to_string(
            'checkout/emails/email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/emails/email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    context = {
        "form": form,
    }

    return render(request, 'contact/contact.html', context)