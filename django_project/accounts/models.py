from django.db import models
from django.conf import settings


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profile'