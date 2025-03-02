from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images/users/", null=True)
    description = models.TextField(null=True)


class HostItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/users/hosts/")
    price = models.IntegerField()
    discount = models.IntegerField()
    description = models.TextField()


class HostItemImages(models.Model):
    id = models.AutoField(primary_key=True)
    host_item = models.ForeignKey(HostItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/users/hosts/images/")

class Chats(models.Model):
    id = models.AutoField(primary_key=True)
    hoster = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name="user_hoster")
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name="user_receiver")
    host = models.ForeignKey(HostItem, on_delete=models.CASCADE)
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chats, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    host = models.ForeignKey(HostItem, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField(default=3)
    date = models.DateTimeField(auto_now_add=True)
