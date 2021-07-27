from django.shortcuts import render
from django.views.generic import (View,TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class BakListView(ListView):
    context_object_name='bakhoods'
    model = models.Bakhood

class BakDetailView(DetailView):
    context_object_name ='bakhood_detail'
    model = models.Bakhood
    template_name = 'basic_app/bakhood_detail.html'

class BakCreateView(CreateView):
    fields = ('name','real_name','fav_p')
    model = models.Bakhood
    
class BakUpdateView(UpdateView):
    fields = ('real_name','fav_p')
    model = models.Bakhood
    
class BakDeleteView(DeleteView):
    model = models.Bakhood
    success_url = reverse_lazy('app:baklist')