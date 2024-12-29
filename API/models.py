from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名")
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="student_created",
        verbose_name="创建者",
    )
    relation = models.ManyToManyField(
        User,
        blank=True,
        related_name="student_shared",
        verbose_name="其他家长",
    )


class Activity(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, verbose_name="活动名称")
    content = models.TextField(blank=True, null=True, verbose_name="活动内容")
    score = models.IntegerField(default=0, verbose_name="分数")
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="创建者",
        related_name="activities_created",
    )
    shared = models.ManyToManyField(
        User,
        blank=True,
        verbose_name="分享用户",
        related_name="activities_shared",
    )

    def __str__(self):
        return f"{self.name} - {self.score} - {self.creator.username}"


class StudentActivity(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True, verbose_name="备注")
    earned_score = models.IntegerField(default=0, verbose_name="获得分数")

    def __str__(self):
        return f"{self.student.name} - {self.activity.name} - {self.earned_score} - {self.create_time}"


def get_total_score(student):
    total_score = StudentActivity.objects.filter(student=student).aggregate(
        total_score=Sum("earned_score")
    )["total_score"]
    return total_score or 0
