from rest_framework import serializers
from .models import *

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ["id", "name", "content", "created_at"]

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ["id", "first_name", "last_name", "email", "phone", "created_at"]

    def create(self, validated_data):
        # Ensure the phone number is normalized before creating the instance
        phone = validated_data.get('phone')

        # Normalize the phone number
        accounts_instance = Accounts(
            **validated_data
        )
        accounts_instance.phone = accounts_instance.normalize_phone_number()

        # Save the instance to the database
        accounts_instance.save()
        return accounts_instance