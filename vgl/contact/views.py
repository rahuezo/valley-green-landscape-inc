from django.shortcuts import render


def contact_view(request):
    context = {}

    return render(request, 'contact/contact.html', context)
