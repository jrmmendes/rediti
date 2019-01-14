from django.db import models

# Create your models here.


class IndexedTimeStampedModel(models.Model):
    """ Model to register edition and creation dates """
    created = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
