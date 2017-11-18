from django.views import generic
from  .models import Linhvuc,Sanpham,Cacsanpham
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
class linhvuc(generic.ListView):
    template_name = 'Trangchu/Linhvuc.html'
    context_object_name = 'List'
    def get_queryset(self):
        return Linhvuc.objects.all()
class cacsanpham(generic.ListView):
    template_name = 'Trangchu/Cacsanpham.html'
    context_object_name = 'CSP'
    def get_queryset(self):
        return Sanpham.objects.all()
class sanpham(generic.DetailView):
    template_name = 'Trangchu/Sanpham.html'
    model = Sanpham
def dangki(request):
    if request.method=='POST':
        form=formdangki(request.POST)
        if form.is_valid():
            nguoidung=User.objects.create_user(username=form.cleaned_data['tentk'],password=form.cleaned_data['matkhau1'])
            return HttpResponseRedirect('/')
        return render(request,'Trangchu/Dangki.html',{'form':form})
    form=formdangki()
    return render(request,'Trangchu/Dangki.html',{'form':form})

