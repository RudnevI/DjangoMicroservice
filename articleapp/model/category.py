from django.db import models


class Category(models.Model):
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
