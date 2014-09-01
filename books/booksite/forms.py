# -*- coding: utf-8 -*-
from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
