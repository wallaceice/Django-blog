from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 55)
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Blog Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    post_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    category = models.CharField(max_length = 55,default='uncategorized')


    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("article_detail", kwargs={"pk": self.pk})
        return reverse("home")
