from django.shortcuts import render, get_object_or_404
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

def rules(request):
    return render(request, "pages/rules.html")

def goals(request):
    return render(request, "pages/goals.html")

def about(request):
    return render(request, "pages/about.html")


# def experiment_delete(request, pk):
#     instance = get_object_or_404(Experiment, pk=pk)

#     if request.user == instance.author:
#         instance.delete()

#     return redirect("experiments_list")