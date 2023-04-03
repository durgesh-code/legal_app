from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from department.models import Department
# Create your models here.

#user BaseUserManage given by django framework for user athonetication and authorization 
class UserManager(BaseUserManager):
    def create_user(self , email , role , password=None):

        if email is None:
            raise ValueError("User must have a email address")

        user= self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)

        return user

class User(AbstractBaseUser):
    ROLES = (
        ('admin' , 'Admin'),
        ('bussinesteam' , 'Bussinesteam'),
        ('legalteam' , 'Legalteam')
    )

    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(verbose_name="user email" , max_length=225 , unique=True , null=False , blank=False)
    name = models.CharField(verbose_name="user full name" , max_length=225 , null=False , blank=False)
    role  = models.CharField(max_length=25 , choices=ROLES , null=False , blank=False)
    department = models.ForeignKey(Department , models.SET_DEFAULT , blank=True , null=True , default=None)
    employee_id = models.BigIntegerField(null=True , blank=True , verbose_name="user employee id")
    password = models.CharField(max_length=128 , null=False , blank=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    object = UserManager()
    USERNAME_FIELD = 'email'

