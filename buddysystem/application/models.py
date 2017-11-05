from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.TextField(max_length=500, blank=True)
    dep_location = models.TextField(max_length=500, blank=True)
    destination = models.TextField(max_length=500, blank= True)
    firstname = models.TextField(max_length=500, blank= True)
    score = models.IntegerField(default=0, blank=True) # thumbs up count
    num_companions = models.CharField(max_length=254, blank = True)
    desired_companions = models.TextField(max_length=500, blank= True) # men, women, anyone

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
