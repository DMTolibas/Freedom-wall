from django.db import models

# Create your models here.
class Rant(models.Model):
    title = models.CharField(max_length=300)
    poster = models.CharField(max_length=100, default="Anonymous")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title