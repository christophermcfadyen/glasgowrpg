from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

#authentication model can be used as player model.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    displayname = models.CharField(max_length = 20, unique = True)
    academic_score = models.IntegerField(default = 0)
    social_score = models.IntegerField(default = 0)

    #stats
    no_grads = models.IntegerField(default=0, blank=False, null=False)
    no_viper = models.IntegerField(default=0, blank=False, null=False)
    no_homework = models.IntegerField(default=0, blank=False, null=False)
    no_tennent = models.IntegerField(default=0, blank=False, null=False)
    no_drop = models.IntegerField(default=0, blank=False, null=False)

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

