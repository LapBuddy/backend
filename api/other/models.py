from django.db import models
from django.contrib.auth.admin import User

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)


class Setup(models.Model):
    user = models.ForeignKey(User, related_name="setups", on_delete=models.CASCADE, blank=False)
    make = models.CharField(max_length=50, blank=False)
    model = models.CharField(max_length=50, blank=False)
    year = models.IntegerField(blank=False)
    tires = models.CharField(max_length=100, blank=True, default="")
    pressure = models.CharField(max_length=50, blank=True, default="")
    suspension = models.CharField(max_length=100, blank=True, default="")
    other = models.CharField(max_length=1000, blank=True, default="")


class Session(models.Model):
    user = models.ForeignKey(User, related_name="sessions", on_delete=models.CASCADE, blank=False)
    track = models.CharField(max_length=100, blank=True, default="")
    file = models.FileField(upload_to="uploads/")
    notes = models.TextField(max_length=1000, blank=True, default="")