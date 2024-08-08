from django.shortcuts import render
from .models import Company
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('ceo','location')

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('listcompany')




















