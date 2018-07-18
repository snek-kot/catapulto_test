from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from modul.testplan.models import TestPlan
from modul.testplan.forms import PlanNewForm, PlanEditForm
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse


class PlanListView(generic.ListView):
    model = TestPlan
    paginate_by = 10
    template_name = '../templates/testplan/list.html'

    def get_queryset(self):
        qs = super().get_queryset()

        filters = {}

        data = self.request.GET
        if 'status' in data:
            filters['status'] = data['status'].capitalize()
        qs = qs.filter(**filters)
        return qs


class DashboardView(generic.ListView):
    model = TestPlan
    template_name = '../templates/testplan/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        counted_al = TestPlan.objects.filter().count()
        counted_pass = TestPlan.objects.filter(status='Done').count()
        counted_error = TestPlan.objects.filter(status='Error').count()
        context['counted_all'] = counted_al
        context['counted_pass'] = counted_pass
        context['counted_error'] = counted_error
        return context


class NewCreateView(generic.CreateView):
    model = TestPlan
    form_class = PlanNewForm
    template_name = 'testplan/new.html'

    def form_valid(self, form):
        intstans = form.save(commit=False)
        intstans.user = self.request.user
        intstans.save()
        self.success_url = reverse('plan:edit', args=[str(intstans.pk)])
        return super().form_valid(form)


class ViewDetailView(generic.DetailView):
    model = TestPlan
    template_name = 'testplan/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['plancase_list'] = instance.plancase_set.filter()
        return context


class EditUpdateView(generic.UpdateView):
    model = TestPlan
    template_name = 'testplan/edit.html'
    form_class = PlanEditForm

    def form_valid(self, form):
        intstans = form.save(commit=False)
        intstans.user = self.request.user
        intstans.save()
        self.success_url = reverse('plan:list')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['plancase_list'] = instance.plancase_set.filter()
        return context

# Create your views here.
