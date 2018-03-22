from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

#authentication model can be used as player model.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    displayname = models.CharField(max_length = 20, unique = True)
    academic_score = models.IntegerField(default = 0)
    social_score = models.IntegerField(default = 0)
    
    slug = models.SlugField()#modified
    #website = models.URLField(blank=True)#there if you want it
    picture = models.ImageField(upload_to='profile_images', blank=True)#modified

    #new method#
    def save(self, *args, **kwargs):#
        self.slug = slugify(self.displayname)#
        super(UserProfile, self).save(*args, **kwargs)#
        
    class Meta():
        verbose_name_plural = "Players"

    def __str__(self):
        return self.user.username

class Game(models.Model):
    status = models.IntegerField(default = 0)
    name = models.CharField(max_length = 20)

    class Meta():
        verbose_name_plural = "Games"

    def __str__(self):
        return self.name

class Question(models.Model):
    question_no = models.IntegerField(default = 0)
    question_text = models.CharField(max_length = 100)

    def __str__(self):
        return self.question_no
