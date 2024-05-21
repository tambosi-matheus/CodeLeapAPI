from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
