from django.db import models
from django.contrib.auth.models import User


# class UserProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     pfp = models.ImageField(upload_to='pfp', default='pfp/default.png')

class EnggModel(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)

    class Meta:
        abstract = True
        db_table = 'enggDB'


class CSE(EnggModel):
    class Meta:
        db_table = 'cse'
        app_label = 'gradubtBackend'


class EEE(EnggModel):
    class Meta:
        db_table = 'eee'
        app_label = 'gradubtBackend'
