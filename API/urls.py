from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, StudentActivityViewSet


router = DefaultRouter()
router.register(r"activities", ActivityViewSet)
router.register(r"student_activities", StudentActivityViewSet)

urlpatterns = router.urls
