import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Cat(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
            )
    created_on = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=200)
    detect = models.ImageField(upload_to='detects/',blank=True)

    def __str__(self):
        return self.created_on

    def get_absolute_url(self):
        return reverse('cat_detail',args=[str(self.id)])

