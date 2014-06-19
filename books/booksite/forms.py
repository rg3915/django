# http://lab305.com/news/2012/jul/19/django-inline-formset-underscore/
from django import forms
from django.forms.models import inlineformset_factory
from .models import Author, Book


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author


class BookForm(forms.ModelForm):

    class Meta:
        model = Book


BookFormSet = inlineformset_factory(Author, Book)
