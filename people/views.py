# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import *

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')
