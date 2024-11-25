from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Activity(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, verbose_name="活动名称")
    content = models.TextField(blank=True, null=True, verbose_name="活动内容")
    score = models.IntegerField(default=0, verbose_name="分数")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "活动"
        verbose_name_plural = "活动管理"


class StudentActivity(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True, verbose_name="备注")
    earned_score = models.IntegerField(default=0, verbose_name="获得分数")

    def __str__(self):
        return f"{self.student.username} - {self.activity.name}"

    class Meta:
        verbose_name = "活动记录"
        verbose_name_plural = "活动记录管理"


def get_total_score(student):
    total_score = StudentActivity.objects.filter(student=student).aggregate(
        total_score=Sum("earned_score")
    )["total_score"]
    return total_score if total_score is not None else 0
