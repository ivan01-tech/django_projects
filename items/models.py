from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    done = models.BooleanField(default=False)