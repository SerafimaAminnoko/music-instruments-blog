from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


# Create your views here.
from .models import *
title = ['Главная страница',"Духовые", "Струнные", "Клавишные", "Ударные","Смычковые",
         ]


def mainpage(request):
    intro = Mainpage.objects.all()
    return render(request, 'mainapp/mainpage.html', {'intro': intro, 'title': title[0]})


def wind(request):
    mus_tab = Musinst.objects.filter(pk=1)
    return render(request, 'mainapp/wind.html', {'mus_tab': mus_tab, 'title': title[1]})


def stringed(request):
    mus_tab = Musinst.objects.filter(pk=4)
    return render(request, 'mainapp/stringed.html', {'mus_tab': mus_tab, 'title': title[2]})


def keyboards(request):
    mus_tab = Musinst.objects.filter(pk=2)
    return render(request, 'mainapp/keyboards.html', {'mus_tab': mus_tab, 'title': title[3]})


def drums(request):
    mus_tab = Musinst.objects.filter(pk=5)
    return render(request, 'mainapp/drums.html', {'mus_tab': mus_tab, 'title': title[4]})

def bowed(request):
    mus_tab = Musinst.objects.filter(pk=3)
    return render(request, 'mainapp/bowed.html', {'mus_tab': mus_tab, 'title': title[5]})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


