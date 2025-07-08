from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('chef/', views.chef, name='chef'),
    path('feature/', views.feature, name='feature'),
    path('blog/', views.blog, name='blog'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),        
]
