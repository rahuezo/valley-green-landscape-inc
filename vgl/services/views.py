from django.shortcuts import render


def services_view(request):
    context = {

    }
    return render(request, 'services/services.html', context)
