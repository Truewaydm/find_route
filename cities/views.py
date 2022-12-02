from django.shortcuts import render

from cities.models import City

# Create your views here.

__all__ = (
    'home',
)


def home(request):
    qs = City.objects.all()
    context = {'objects_list': qs}
    return render(request, 'cities/home.html', context)
