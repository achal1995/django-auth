from django.db import models

# Create your models here.

# Getting current user model
from django.contrib.auth import get_user_model
Users = get_user_model()

class OauthAccessToken(models.Model):
    """Access token."""
    owner=models.OneToOneField(Users, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255, unique=True)
    expiry_at = models.CharField(max_length=255)

    class Meta:
        db_table = 'oauth_access_token'
    
    def __str__(self):
        return self.access_token


class OauthRefreshToken(models.Model):
    """Refresh token."""
    owner=models.OneToOneField(Users, on_delete=models.CASCADE)
    refresh_token = models.CharField(max_length=255, unique=True)
    expiry_at = models.CharField(max_length=255)

    class Meta:
        db_table = 'oauth_refresh_token'
    
    def __str__(self):
        return self.refresh_token