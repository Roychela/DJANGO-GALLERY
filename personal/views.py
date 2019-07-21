from django.shortcuts import render
from .models import Image, Category, Location
# Create your views here.
def welcome(request):
    images = Image.get_all_images()
    return render(request, 'welcome.html', {"images": images})