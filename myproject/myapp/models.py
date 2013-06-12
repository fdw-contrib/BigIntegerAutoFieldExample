from django.db import models

from django.db import models
from myapp import bigint_patch

class VeryLargeModel(models.Model):
    id = bigint_patch.BigAutoField(primary_key=True)
    data = models.TextField()

class ReferencingModel(models.Model):
    id = bigint_patch.BigAutoField(primary_key=True)
    target = bigint_patch.BigForeignKey(VeryLargeModel)
    more_data = models.TextField()
