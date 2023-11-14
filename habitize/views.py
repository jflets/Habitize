from django.shortcuts import render

def custom_404_view(request, exception):
    """
    View function for handling 404 errors.

    Renders a custom 404 error page.
    """
    return render(request, '404.html', status=404)

def custom_500_view(request):
    """
    View function for handling 500 errors.

    Renders a custom 500 error page.
    """
    return render(request, '500.html', status=500)

def custom_403_view(request, exception):
    """
    View function for handling 403 errors.

    Renders a custom 403 error page.
    """
    return render(request, '403.html', status=403)
