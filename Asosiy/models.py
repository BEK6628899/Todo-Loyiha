from django.db import models
from django.contrib.auth.models import User



class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    st_raqam = models.CharField(max_length=10)
    kurs = models.PositiveSmallIntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)    #user1
    def __str__(self):
        return self.ism


class Todo(models.Model):
    plan = models.CharField(max_length=100)
    time = models.DateTimeField()
    description = models.TextField()
    foydalanuvchi = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.plan

