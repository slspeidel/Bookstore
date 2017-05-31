# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book
from django.contrib.sites.requests import RequestSite

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    """
    This class is used for database administration
    The "list_display" sets the fields that show in the adminstration list
    """
    list_display = ('title', 'author', 'price', 'stock')

admin.site.register(Book, BookAdmin)
