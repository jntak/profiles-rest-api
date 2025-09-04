from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""

    def create_user(self, email, name, password=None, **extra_fields):
        """Create and return a new user"""
        
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        
        # hash password
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, name, password, **extra_fields):
        """Create and return a new superuser"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, name, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email
    
class ProfileFeedItem(models.Model):
    """ Update Profile Status """
    
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    status_text = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def ___str___(self):
        return f"{self.user_profile.name}"
