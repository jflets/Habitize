from django.shortcuts import render, redirect


def landingPage(request):
    return render(request, 'landing_page/index.html')
