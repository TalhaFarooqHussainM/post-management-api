from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    customer = models.ForeignKey(Customer, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, related_name='image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.image.url
