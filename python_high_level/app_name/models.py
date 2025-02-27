from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Accounts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(
        max_length=50,
        validators=[
                RegexValidator(
                    regex=r'^[a-zA-Z-]{2,}$',  # Can only contain uppercase, lowercase, and hyphens
                    message="Name must be at least 2 characters can only contain uppercase letters, lowercase letters, and hyphens"
                )
            ]
    )
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name