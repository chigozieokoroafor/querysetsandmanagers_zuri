from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

from links.managers import ActiveLinkManager

# Create your models here.
User = get_user_model()

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super().save(*args, **kwargs)
        pass 
    
    def __str__(self) -> str:
        return self.identifier