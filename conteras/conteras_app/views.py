from django.shortcuts import render

def load(request):
    return render(request, 'conteras_app/load.html')

def choose(request):
    return render(request, 'conteras_app/choose.html')

def fhome(request):
    return render(request, 'conteras_app/fhome.html')

def mhome(request):
    return render(request, 'conteras_app/mhome.html')

def settings(request):
    return render(request, 'conteras_app/settings.html')