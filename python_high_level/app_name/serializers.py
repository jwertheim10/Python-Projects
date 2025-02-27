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