from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from mailing.models import Client


def index(request):
    return render(request, 'mailing/index.html')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('mailing:clients_list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('mailing:clients_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients_list')