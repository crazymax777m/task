from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import CustomUserCreationForm
from .models import Car, CustomUser
from .serializers import PersonSerializer, CarSerializer


class PersonDetail(DetailView):
    model = CustomUser
    template_name = 'cars/person.html'
    context_object_name = 'person'


class PersonView(ListView):
    model = CustomUser
    template_name = 'cars/index.html'
    context_object_name = 'persons'


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'cars/register.html'
    success_url = reverse_lazy('cars:1')
    # def get_success_url(self):
    #     print(self.kwargs)
    #     return 'ok'


class PersonViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication,)
