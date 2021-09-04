from users.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    description = models.TextField()
    image = models.URLField(max_length=255)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    up_vote = models.IntegerField()
    down_vote = models.IntegerField()