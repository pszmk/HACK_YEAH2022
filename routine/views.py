from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# Create your views here.
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Routine


class RoutineList(ListView):
    model = Routine
    template_name = 'routine/home.html'
    context_object_name = 'items'
    paginate_by = 5
    # ordering = ['-create']
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()  
        return self.render_to_response(context)



class RoutineCreate(FormView):    
    model = Routine
    fields = ["routine_title"]
    success_url = reverse_lazy('routines')
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RoutineCreate, self).form_valid(form)



class RegisterPage(FormView):
    template_name = 'routine/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('songs')
    
