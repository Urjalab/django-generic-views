from django.db import models
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.id})
    

    class Meta:
        ordering = (
            '-created_at', 
            '-modified_at',
        )



