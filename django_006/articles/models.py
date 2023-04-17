from django.db import models
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    emote_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='emote_articles')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comments")

class Emote(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=10)
    