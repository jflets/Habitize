from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def custom_500_view(request):
    return render(request, '500.html', status=500)


def custom_403_view(request, exception):
    return render(request, '403.html', status=403)
