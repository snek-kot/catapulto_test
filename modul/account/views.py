from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse
from modul.account.forms import NewAccountForm, LoginAccountForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView


class NewAccountView(generic.CreateView):
    model = User
    template_name = 'account/sign_in.html'
    form_class = NewAccountForm

    def form_valid(self, form):
        intstans = form.save(commit=False)
        intstans.user = self.request.user
        intstans.save()
        self.success_url = reverse('account:login')
        return super().form_valid(form)
#UserCreationForm


class LoginAccountView(FormView):
    model = User
    template_name = 'account/login.html'
    form_class = LoginAccountForm
    success_url = 'plan:list'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())



