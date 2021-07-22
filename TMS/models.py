from django.db import models

# Create your models here.

class TMS(models.Model):
    classroom = models.CharField(max_length=120)
    building = models.TextField()
    completed = models.BooleanField(default=False)
    seats = models.IntegerField()
    rows = models.IntegerField(default = 30)
    columns = models.IntegerField(default = 30)

    def _str_(self):
        return self.title