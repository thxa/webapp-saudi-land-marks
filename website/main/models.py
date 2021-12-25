from django.contrib.auth.models import User
from django.db import models

class Landmark(models.Model):

    name = models.CharField(max_length=50,null=False, blank=True)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    about =  models.TextField()
    photo_url = models.URLField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    
    owner = models.ForeignKey(User, related_name='landmarks', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/landmarks/%d/' % self.pk

    class Meta:
        ordering = ['created', 'name']