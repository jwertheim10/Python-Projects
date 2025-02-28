from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
import re

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
    email = models.EmailField(max_length=255)
    phone = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^(\(\d{3}\)\s?\d{3}-\d{4}|\d{1}-\d{3}-\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4})$',
                message="Phone number must be in one of the following forms: (XXX) XXX-XXXX, X-XXX-XXX-XXXX, XXX-XXX-XXXX, XXX.XXX.XXXX"
            ),
            ]      
                             )
    created_at = models.DateTimeField(auto_now_add=True)

    def normalize_phone_number(self):
    # Remove all non-numeric characters
        phone = str(self.phone).strip()
        digits_only = re.sub(r'\D', '', phone)

        # Ensure the phone number has exactly 10 digits
        if len(digits_only) == 10:
            return f"{digits_only[:3]}-{digits_only[3:6]}-{digits_only[6:]}"
        elif len(digits_only) == 11:
            return f"{digits_only[1:4]}-{digits_only[4:7]}-{digits_only[7:]}"
        else:
            raise ValueError("Invalid phone number format. Phone number should contain 10 or 11 digits.")
        
    def save(self, *args, **kwargs):
        # Normalize phone number before saving
        self.phone = self.normalize_phone_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name