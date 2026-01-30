from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path("", views.home, name="home"),
    path('new-page/', views.new_page, name='new_page'),
]