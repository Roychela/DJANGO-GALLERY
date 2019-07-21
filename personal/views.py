from django.shortcuts import render
from .models import Image, Category, Location
# Create your views here.
def welcome(request):
    images = Image.get_all_images()
    return render(request, 'welcome.html', {"images": images})

def search_image(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',
                      {'images': images, 'message': message, 'categories': categories,
                       "locations": locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html', {"message": message})