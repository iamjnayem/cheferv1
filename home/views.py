from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    """
    Render the home page.
    """
    return render(request, 'home/home.html')


def about(request):
    """
    Render the about page.
    """
    return render(request, 'home/about.html')   

def menu(request):
    """
    Render the menu page.
    """
    return render(request, 'home/menu.html')    

def chef(request):
    """
    Render the chef page.
    """
    return render(request, 'home/chef.html')    

def feature(request):
    """
    Render the feature page.
    """
    return render(request, 'home/feature.html') 

def blog(request):
    """
    Render the blog page.
    """
    return render(request, 'home/blog.html')    

def testimonial(request):
    """
    Render the testimonial page.
    """
    return render(request, 'home/testimonial.html') 


def contact(request):
    """
    Render the contact page.
    """
    return render(request, 'home/contact.html') 