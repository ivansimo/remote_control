from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        n_serie = request.POST['n_serie']
        modelo = request.POST['modelo']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        cliente_email = request.POST['cliente_email']


        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(n_serie=n_serie, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Ya has solicitado esta operación')
                return redirect('/grupos')

        contact = Contact(n_serie=n_serie, modelo=modelo, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        send_mail(
        'Subject',
        'Message.',
        'isimosanchez@gmail.com',
        ['isimosanchez@gmail.com', 'ivansimo@industria40.me'],
        )

        messages.success(request, 'Tu solicitud ha sido enviada, pronto actualizaremos la información')

        return redirect('/grupos')
