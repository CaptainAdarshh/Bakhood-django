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

class SonCreateView(CreateView):
    fields = ('name','age','father')
    model = models.Sons
    
class SonUpdateView(UpdateView):
    fields = ('age','father')
    model = models.Sons
    
class SonDeleteView(DeleteView):
    model = models.Sons
    success_url = reverse_lazy('app:baklist')
    
class SonListView(ListView):
    context_object_name='sons'
    model = models.Sons

class SonDetailView(DetailView):
    context_object_name ='sons_detail'
    model = models.Sons
    template_name = 'basic_app/sons_detail.html'