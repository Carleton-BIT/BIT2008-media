from django.db import models
from django.conf import settings



class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='task_images/', default='default.jpg')

    def __str__(self):
        return self.description