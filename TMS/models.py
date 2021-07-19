from django.db import models

# Create your models here.

class TMS(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    places = models.IntegerField()

    def _str_(self):
        return self.title