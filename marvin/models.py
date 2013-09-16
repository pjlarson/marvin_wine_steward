from django.db import models

class Grape(models.Model):
    common_name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)

