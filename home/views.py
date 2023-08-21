from django.shortcuts import render


def index(request):
    """
    A view to display the index page
    """
    return render(request, 'home/index.html')


def privacy(request):
    """
    A view to display the privacy policy page
    """
    return render(request, 'home/privacy.html')

def delivery(request):
    """
    A view to display the privacy policy page
    """
    return render(request, 'home/delivery.html')

