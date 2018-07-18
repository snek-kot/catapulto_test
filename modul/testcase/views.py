from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from modul.testcase.models import TestCase, LogCase
from modul.testcase.forms import TestCaseForm

from django.views import generic


class CaseListView(generic.ListView):
    model = TestCase
    template_name = 'testcase/list.html'


class NewView(generic.CreateView):
    model = TestCase
    form_class = TestCaseForm
    template_name = 'testcase/new .html'


class EditDetailView(generic.DetailView):
    model = TestCase
    template_name = 'testcase/edit.html'


class ViewDetailView(generic.DetailView):
    model = TestCase
    template_name = 'testcase/view .html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LogCase_list'] = LogCase.objects.filter()
        return context
