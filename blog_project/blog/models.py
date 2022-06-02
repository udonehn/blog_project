from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 60)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(blank = True)
    
    def __str__(self):
        return f'{self.title} - {self.id}'