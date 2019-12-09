from django.db import models
from django.contrib.auth.hashers import make_password,check_password


class User(models.Model):
    class Meta:
        db_table = 'user'

    name = models.CharField(max_length=20,null=True,unique=True)
    password = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    def _set_password(self,password):
        self.password = make_password(password)

    def _check_password(self,password):
        return check_password(password,self.password)

	
