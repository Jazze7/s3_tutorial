from django.db import models

class Post(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField( max_length=254)
    image=models.ImageField( upload_to="posts/")

    def __str__(self):
        return self.name