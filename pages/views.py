from django.shortcuts import render

from django.views.generic import TemplateView

class HOmePageView(TemplateView):
    template_name = 'home.html'