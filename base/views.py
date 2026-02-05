from django.shortcuts import render
from .models import Profile

# Create your views here.
  
def home(request):
    profile = Profile.objects.first()  # Получаем первый профиль для отображения
    return render(request, "home.html", {'profile': profile})

def new_page(request):
    return render(request, 'new_page.html')