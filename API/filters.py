from rest_framework import filters


class StudentFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(creator=request.user)


class ActivityFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(creator=request.user)


class StudentActivityFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(
            student__creator=request.user,
            student=request.query_params.get("student"),
        )
