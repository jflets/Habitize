from django.shortcuts import render
from django.http import HttpResponse


def landingPage(request):
    return render(request, 'landing_page/index.html')
