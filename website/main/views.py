from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView
from .models import Landmark
import random

def index(request):
    landmarks = Landmark.objects.all()
    context = {
        "landmarks": landmarks 
    }
    return render(request, "index.html", context)

def landmark(request, landmark_id):
    landmark = get_object_or_404(Landmark, pk=landmark_id)
    max_id = Landmark.objects.order_by('-id')[0].pk
    random_id = random.randint(1, max_id + 1)
    random_landmarks = Landmark.objects.filter(id__gte=random_id)[:3]

    context = {
        "landmark": landmark, 
        "random_landmarks": random_landmarks 
    }
    return render(request, "pages/content.html", context)

def landmark_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            place = request.POST.get("place")
            city = request.POST.get("city")
            about = request.POST.get("about")
            photo_url = request.POST.get("photo_url")
            Landmark.objects.create(name=name, place=place, city=city,
                                    about=about, photo_url=photo_url, 
                                    owner=request.user)    
            return HttpResponseRedirect("/account/")
        return render(request, "pages/create.html")
    return HttpResponseRedirect("/")

def landmark_update(request, landmark_id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Landmark, pk=landmark_id)
        if request.user == instance.owner:
            if request.method == "POST":
                name = request.POST.get("name")
                place = request.POST.get("place")
                city = request.POST.get("city")
                about = request.POST.get("about")
                photo_url = request.POST.get("photo_url")
                    
                instance.name = name
                instance.place = place
                instance.place = place
                instance.city = city
                instance.about = about
                instance.photo_url = photo_url

                instance.save()
            return render(request, "pages/update.html", { "landmark": instance })
    return HttpResponseRedirect("/landmarks/%d/" % landmark_id)

def landmark_delete(request, landmark_id):
    instance = get_object_or_404(Landmark, pk=landmark_id)
    if request.user.is_authenticated and request.user == instance.owner:
        instance.delete()  
        return HttpResponseRedirect("/account/")
    return HttpResponseRedirect("/landmarks/%d/" % landmark_id)
def rules(request):
    return render(request, "pages/rules.html")

def goals(request):
    return render(request, "pages/goals.html")

def about(request):
    return render(request, "pages/about.html")



