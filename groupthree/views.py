#-*- coding: utf-8 -*-
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from groupthree.forms import LoginForm, SalaCreateForm
from django_datatables_view.base_datatable_view import BaseDatatableView


class Login(LoginView):
    authentication_form = LoginForm


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'groupthree/home.html'

    def get_context_data(self, *arg, **kwargs):
        context = super(Home, self).get_context_data(*arg, **kwargs)
        return context


class SalaPublicaListView(LoginRequiredMixin, TemplateView):
    template_name = 'groupthree/sala_publica.html'

    def get_context_data(self, *arg, **kwargs):
        context = super(SalaPublicaListView, self).get_context_data(*arg, **kwargs)
        return context


class SalaCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'groupthree/crear_sala.html'

    def get_context_data(self, *arg, **kwargs):
        context = super(SalaCreateView, self).get_context_data(*arg, **kwargs)
        context['form'] = SalaCreateForm()
        return context
