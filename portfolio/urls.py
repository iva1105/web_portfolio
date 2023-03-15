from portfolio import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.handleblog, name='handleblog'),
    
]