from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')  # whenerver someone uploads an image, path where it should be saved
    summary = models.CharField(max_length=200)      # description of that image giving it a specific length
