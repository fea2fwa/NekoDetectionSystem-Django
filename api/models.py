from django.db import models


class Cat(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=200, blank=True, null=True)
    detect = models.ImageField(upload_to='detects/',blank=True)

