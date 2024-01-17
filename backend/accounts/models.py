from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('이메일을 입력해주세요.')
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
            **extra_fields
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser
    

class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
        ('N', '무응답')
    ]
    
    email = models.EmailField(unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(max_length=25)
    nickname = models.CharField(max_length=25, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N') 
    phone = models.CharField(max_length=10, unique=True)
    introduce = models.CharField(max_length=300, blank=True)
    profile_image = models.ImageField(upload_to='media/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField('self', symmetrical=False, through='Follower')
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    
    
    def follower_count(self):
        return self.followers.count()
    
    
class Follower(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_set')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    created_at = models.DateTimeField(auto_now_add=True)