from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.validators import MaxValueValidator
from django.urls import reverse

from .utils import unique_slug_generator

# Create your models here.

class Laptop(models.Model):
    name       = models.CharField(max_length=120, null=False, blank= False, help_text=' Enter a Laptop Name. E.g Acer')
    quantity   = models.PositiveIntegerField(validators=[MaxValueValidator(500),], null=False, blank= False, help_text=' Please Enter Quantity to store. Note Cannot exceed 500')
    timestamp  = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)
    slug       = models.SlugField(null=True, blank= True)


    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug":self.slug})


def lp_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(lp_pre_save_receiver, sender=Laptop)

