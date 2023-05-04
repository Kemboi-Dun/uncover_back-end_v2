from django.db import models
from datetime import date


CATEGORIES = (
    ("art", "Art"),
    ("technology", "Technology"),
     ("music", "Music"),
      ("food", "Food"),
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100,default="Kemboi Duncan", null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    author_image = models.ImageField(upload_to='images/', null=True, blank=True)
    date = models.DateField(("Date"), default=date.today)
    categories = models.CharField(max_length = 20, choices = CATEGORIES)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
