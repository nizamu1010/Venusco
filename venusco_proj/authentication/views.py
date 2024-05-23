from django.shortcuts import render



def home(request):
    return render(request, 'index.html')


def fullstack(request):
    return render(request, 'fullstack.html')