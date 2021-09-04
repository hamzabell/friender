from django.db import models
from users.models import User
# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    subcriber = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='subscriber')
    subcribed_when = models.DateTimeField(auto_now_add=True)
