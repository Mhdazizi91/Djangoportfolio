from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)  # whenerver someone uploads an image, path where it should be saved
    pub_date = models.DateTimeField()  # description of that image giving it a specific length
    body = models.TextField(max_length=200)  # description of that image giving it a specific length
    image = models.ImageField(upload_to='Blogimages/')  # whenerver someone uploads an image, path where it should be saved