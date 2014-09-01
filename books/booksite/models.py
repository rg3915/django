# -*- coding: utf-8 -*-
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    CATEGORIES = [
        ('romance', 'Romance'),
        ('fiction', u'Ficção'),
        ('suspense', 'Suspense')
    ]
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORIES)
