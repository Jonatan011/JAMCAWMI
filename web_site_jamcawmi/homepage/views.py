from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "homepage/home.html")

def about(request):
    return render(request, 'homepage/about.html')

def services(request):
    return render(request, 'homepage/services.html')

def portafolio(request):
    return render(request, 'homepage/portafolio.html')

def faq(request):
    return render(request, 'homepage/faq.html')

def contact(request):
    return render(request, 'homepage/contact.html')

def terms(request):
    return render(request, 'homepage/terms.html')

def privacy(request):
    return render(request, 'homepage/privacy.html')

def legal(request):
    return render(request, 'homepage/legal.html')