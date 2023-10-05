from django.shortcuts import render, redirect


def landingPage(request):
    return render(request, 'landing_page/index.html')

def HelpPage(request):
    return render(request, 'landing_page/help.html')

def thankYouPage(request):
    return render(request, 'landing_page/contact-thank-you.html')