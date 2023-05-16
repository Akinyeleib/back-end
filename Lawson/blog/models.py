from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    
    authors = [(user.username, f'{user.first_name} {user.last_name}') for user in User.objects.all()]
    
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, choices=authors, blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        ordering = ['title', 'date']

