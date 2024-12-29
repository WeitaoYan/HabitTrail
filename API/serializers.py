from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # create user 会对密码进行加密
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )
        return user

    class Meta:
        model = User
        fields = ["username", "password", "email"]


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = ["id", "name", "content", "score", "creator"]


class StudentActivitySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["activity"] = instance.activity.name
        data["time"] = instance.create_time.strftime("%m-%d %H:%M")
        return data

    def validate(self, data):
        user = self.context["request"].user

        # 验证 student 是否是用户可以管理的
        if not user.is_staff and data["student"].creator != user:
            raise serializers.ValidationError(
                "You do not have permission to manage this student."
            )

        # 验证 activity 是否是用户创建的
        if data["activity"].creator != user:
            raise serializers.ValidationError(
                "You do not have permission to use this activity."
            )

        return data

    class Meta:
        model = models.StudentActivity
        fields = ["activity", "earned_score", "comment", "operator", "student"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ["id", "name", "creator"]
