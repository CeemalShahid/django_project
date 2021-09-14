from django.db import models

class parking(models.Model):
    cam_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='parking_images',blank=True)
    date  = models.DateTimeField(auto_now_add=True)
