import logging
from rest_framework import decorators, response, generics, viewsets
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers, permissions, models, filters


logger = logging.getLogger("file_console")


class RegisterView(generics.CreateAPIView):
    """这里是正式账号的注册,注册后直接返回token,不需要再次登录"""

    serializer_class = serializers.RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return response.Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


class ActivityViewSet(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    filter_backends = [filters.ActivityFilterBackend]

    def create(self, request, *args, **kwargs):
        request.data["creator"] = self.request.user.pk
        return super().create(request, *args, **kwargs)


class StudentActivityViewSet(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.StudentActivity.objects.all()
    serializer_class = serializers.StudentActivitySerializer
    filter_backends = [filters.StudentActivityFilterBackend]
    pagination_class = None

    def create(self, request, *args, **kwargs):
        request.data["operator"] = self.request.user.pk
        return super().create(request, *args, **kwargs)


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_backends = [filters.StudentFilterBackend]

    def create(self, request, *args, **kwargs):
        request.data["creator"] = self.request.user.pk
        return super().create(request, *args, **kwargs)

    @decorators.action(
        detail=True,
        url_path="totalScore",
        permission_classes=[permissions.IsOwner],
    )
    def total_score(self, request, pk):
        student = self.get_object()
        total_score = models.get_total_score(student)
        return response.Response({"total": total_score})
