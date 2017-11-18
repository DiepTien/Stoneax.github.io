from django.views import generic
from  .models import Chungloai,Linhkien
from django.shortcuts import render
from django.http import HttpResponseRedirect
class chungloai(generic.ListView):
    template_name = 'Cuahang/Chungloai.html'
    context_object_name = 'Chungloais'
    def get_queryset(self):
        return Chungloai.objects.all()
class linhkien(generic.ListView):
    template_name = 'Cuahang/Linhkien.html'
    context_object_name = 'Linhkiens'
    def get_queryset(self):
        return Linhkien.objects.all()
