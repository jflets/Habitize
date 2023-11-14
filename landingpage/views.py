from django.shortcuts import render, redirect

def landingPage(request):
    """
    View function for rendering the landing page.

    Renders the landing page template.
    """
    return render(request, 'landing_page/index.html')

def HelpPage(request):
    """
    View function for rendering the help page.

    Renders the help page template.
    """
    return render(request, 'landing_page/help.html')

def thankYouPage(request):
    """
    View function for rendering the thank you page.

    Renders the thank you page template.
    """
    return render(request, 'landing_page/contact-thank-you.html')
