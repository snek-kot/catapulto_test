from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from modul.testcase.models import TestCase, LogCase
from modul.testcase.forms import TestCaseForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic


@method_decorator(login_required, name='dispatch')
class CaseListView(generic.ListView):
    model = TestCase
    template_name = 'testcase/list.html'


@method_decorator(login_required, name='dispatch')
class NewView(generic.CreateView):
    model = TestCase
    form_class = TestCaseForm
    template_name = 'testcase/new .html'


@method_decorator(login_required, name='dispatch')
class EditDetailView(generic.DetailView):
    model = TestCase
    template_name = 'testcase/edit.html'


@method_decorator(login_required, name='dispatch')
class ViewDetailView(generic.DetailView):
    model = TestCase
    template_name = 'testcase/view .html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LogCase_list'] = LogCase.objects.filter()
        return context
