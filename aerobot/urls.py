from django.urls import path
from . import views
app_name = 'aerobot'
urlpatterns = [
    path('', views.home ,name='home'),
    path('/about', views.about ,name='about'),
    path('/gallery', views.gallery ,name='gallery'),
    path('/blogs', views.blogs ,name='blogs'),
    path('/contact', views.contact ,name='contact'),
]
