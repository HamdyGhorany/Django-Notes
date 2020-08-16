from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save

# Create your models here.

import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    headline = models.CharField(max_length = 150)
    bio = models.TextField()
    img = models.ImageField(upload_to="profile_img")
    join_date = models.DateTimeField(blank=True, default=datetime.datetime.now)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' %(self.user)
    

## signals

def create_profile(sender , **kwargs):
    if kwargs['created']:
        user_profile = profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
    
    
    
    
    
    
