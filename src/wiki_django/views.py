# -*- coding: utf-8 -*-
from django.conf import settings
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['static_url'] = settings.STATIC_URL
        return context
