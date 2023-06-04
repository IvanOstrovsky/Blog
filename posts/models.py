from django.db import models

from users.models import User


# from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='content_images', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='like_post')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
