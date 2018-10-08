from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView , DetailView , FormView , CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

from .forms import LaptopCreateForm

from .models import Laptop

# Create your views here.


class HomePageView(ListView):
    template_name = 'home.html'
    model = Laptop



class LaptopDetailView(DetailView):
    template_name = 'laptop_detail.html'
    model = Laptop


class FormCreateView(CreateView):
    template_name='create_form.html'
    model = Laptop
    fields = ['name', 'quantity']
    #success_url = '/home/'

class LaptopUpdate(UpdateView):
    template_name='update_form.html'
    model = Laptop
    fields = ['name', 'quantity']
    #success_url = '/home/'

class LaptopDelete(DeleteView):
    template_name='delete_form.html'
    model = Laptop
    success_url = reverse_lazy('home')