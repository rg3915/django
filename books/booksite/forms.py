# -*- coding: utf-8 -*-
from django import ModelForm
# from .models import Author


class AuthorForm(ModelForm):

    class Meta:
        model = Author
