from django.shortcuts import render
from django.db import models
from django.views import generic
from django.urls import reverse
from django.contrib.auth.models import User
from modul.account.forms import LoginAccountForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


# class NewAccountView(generic.CreateView):
#     model = User
#     template_name = 'account/sign_in.html'
#     form_class = NewAccountForm
#
#     def form_valid(self, form):
#         intstans = form.save()
#         intstans.user = self.request.user
#         intstans.save()
#         self.success_url = reverse('account:login')
#         return super().form_valid(form)
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
# #UserCreationForm
#
#
# class LoginAccountView(FormView):
#     model = User
#     template_name = 'account/login.html'
#     form_class = LoginAccountForm
#     success_url = 'plan:list'
#
#     def form_valid(self, form):
#         login(self.request, form.get_user())
#         return HttpResponseRedirect(self.get_success_url())


class NewAccountView(FormView):
    form_class = UserCreationForm
    success_url = "/account/login/"
    template_name = "account/sign_in.html"

    def form_valid(self, form):
        form.save()
        return super(NewAccountView, self).form_valid(form)


class LoginAccountView(FormView):
    form_class = AuthenticationForm
    template_name = "account/login.html"
    success_url = "/plan/list"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginAccountView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")