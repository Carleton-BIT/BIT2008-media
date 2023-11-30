from django.db import models
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='task_images/', default='default.jpg')
    video = models.FileField(upload_to='task_videos/', default='EE E EEEE.mp4')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        MAX_SIZE = (500, 500)

        # Open the uploaded image
        img = Image.open(self.image.path)

        if img.height > MAX_SIZE[1] or img.width > MAX_SIZE[0]:

            # Resize the image using LANCZOS filter
            img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)

            # Save the resized image back to self.image
            img_file = BytesIO()
            img.save(img_file, 'JPEG', quality=90)  # Adjust quality as needed
            file_name = self.image.name
            self.image.save(file_name, ContentFile(img_file.getvalue()), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.description