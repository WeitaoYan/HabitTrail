from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"students", views.StudentViewSet, basename="student")

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("activities/", views.ActivityViewSet.as_view(), name="activity"),
    path(
        "studentActivities/",
        views.StudentActivityViewSet.as_view(),
        name="studentActivity",
    ),
    path("", include(router.urls)),
]
