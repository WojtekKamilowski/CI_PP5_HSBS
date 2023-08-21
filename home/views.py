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
    A view to display the delivery policy page
    """
    return render(request, 'home/delivery.html')


def about(request):
    """
    A view to display who we are page
    """
    return render(request, 'home/about.html')


def club(request):
    """
    A view to display the history club page
    """
    return render(request, 'home/club.html')
