from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
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
        message_subject = request.POST.get('subject')
        content = request.POST.get('content')

        subject = render_to_string(
            'contact/emails/email_subject.txt',
            {'subject': message_subject}
        )
        body = render_to_string(
            'contact/emails/email_body.txt',
            {'name': name, 'email': email,
             'content': content}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ['contact@southroast.co.uk']
        )
        messages.success(request, "Thanks for getting in touch!\
                         We'll get back to you as soon as possible.")
        return redirect(reverse('home'))

    context = {
        "form": form,
    }

    return render(request, 'contact/contact.html', context)
