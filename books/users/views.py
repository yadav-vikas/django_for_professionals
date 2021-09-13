from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustUserCreationForm
    success_url = reverse_lazy('login')
    template_name='users/signup.html'
