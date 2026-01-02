from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True , blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self , *args , **kwargs ):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args , **kwargs)


    likes = models.ManyToManyField(
        User,
        related_name='liked_post',
        blank=True
    )

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'commnet by {self.author} on {self.post}'
