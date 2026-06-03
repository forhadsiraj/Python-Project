from django.db import models

class Post(models.Model):
    texts = models.TextField()
    
    def __str__(self):
        return self.texts[:50]