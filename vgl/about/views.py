from django.shortcuts import render


def about_view(request):
    context = {}

    return render(request, 'about/about.html', context)
