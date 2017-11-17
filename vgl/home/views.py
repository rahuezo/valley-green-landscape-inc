# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from utils.get_cities import get_cities


def index(request):
    context = {
        'work_radius': get_cities(),
    }

    return render(request, "home/home.html", context)
