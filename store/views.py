# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book

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
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'store.html', context)

