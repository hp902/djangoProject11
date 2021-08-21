
from django.db import models
# Create your models here.
from django.utils import timezone
from datetime import datetime

from time import gmtime, strftime
from django.contrib.auth.models import User

class cds_model(models.Model):
    now = datetime.now()
    result = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to = "Post",blank=True)
    date = models.TextField(max_length=200, blank=True)


    def __str__(self):
        return str(self.date) + ' '+ str(self.result)


