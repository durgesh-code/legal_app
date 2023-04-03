from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50 , null=False , blank=False)