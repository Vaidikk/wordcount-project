
from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='home'),
    #the "name" is the name by which this page can be directly accessed in {% url %} tag in html
    path('count/', views.count, name='count'),

    path('about/', views.about, name='about'),
]
