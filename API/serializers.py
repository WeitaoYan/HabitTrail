from rest_framework import serializers
from .models import Activity, StudentActivity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["id", "name", "content", "score"]


class StudentActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentActivity
        fields = ["id", "student", "activity", "comment", "earned_score"]
