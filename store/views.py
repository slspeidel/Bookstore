# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    """
    first view
    """
    return render(request, 'template.html')

def store(request):
    """
    second view
    """
    return render(request, 'store.html')

