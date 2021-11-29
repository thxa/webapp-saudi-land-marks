from django.db import models
from django.urls import reverse_lazy

class Landmark(models.Model):

    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    about =  models.TextField()
    photo_url = models.URLField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(blank=True, unique=True)
    # season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="episodes", null=True)
    # owner = models.ForeignKey(User, related_name='landmarks', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     # if not self.id:
    #     #     self.slug = slugify(self.name)

    #     # if not self.photo_url:
    #     #     self.photo_url = self.photo_url

    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return '/landmarks/%d/' % self.id
        # return reverse_lazy('landmarks', args=[self.id])

    class Meta:
        ordering = ['created', 'name']