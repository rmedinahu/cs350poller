# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

class HomeView(generic.TemplateView):
    template_name = 'home.html'