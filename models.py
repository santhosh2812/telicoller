from django.db import models



class User(models.Model):
    Mobile = models.IntegerField(blank=True,null=True)
    Name = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
        verbose_name = "user_table"
        verbose_name_plural = "users_table"

class Callhisory(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    call_to = models.IntegerField(blank=True,null=True)
    Date = models.DateField(blank=True,null=True)
    Duration = models.FloatField(blank=True,null=True)

    class Meta:
        verbose_name = "Callhisory_table"
        verbose_name_plural = "Callhisories_tables"