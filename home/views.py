from django.shortcuts import render
from .models import Person

def home_index(request):
    person = Person.objects.get(pk=1)
    return render(request, 'home_index.html', {"person": person})
