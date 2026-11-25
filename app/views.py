from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service, Request
from .forms import RequestForm

class ServiceListView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'

class RequestCreateView(LoginRequiredMixin, FormView):
    form_class = RequestForm
    template_name = 'new_request.html'
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        req = form.save(commit=False)
        req.user = self.request.user
        req.save()
        return super().form_valid(form)

class PersonalAccountView(LoginRequiredMixin, ListView):
    model = Request
    template_name = 'account.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)