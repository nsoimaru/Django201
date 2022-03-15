from socket import IPV6_JOIN_GROUP
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def creeate_user_profile(sender, instance, created, **kwargs):
    """Create a new Profile() object when a Django User is created"""
    if created:
        Profile.objects.create(user=instance)