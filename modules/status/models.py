from django.db import models
from django.conf import settings

# Create your models here.

def upload_status_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

class StatusQuerySet(models.QuerySet):
    pass

class StatusMananger(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)

class Status(models.Model): # fb status, instagram post, tweet, linkedin post
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=upload_status_image, blank=True, null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = StatusMananger()

    def __str__(self):
        return str(self.content)[:50]


    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status post'
    

    
