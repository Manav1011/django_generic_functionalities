from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()
class KeyStore(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pub = models.TextField()

    def __str__(self):
        return self.user.email