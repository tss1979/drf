from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from school.permissions import IsOwnerPermission
from users.permissions import UserIsModeratorPermission, UserIsStaffPermission

from school.models import Course, Lesson
from school.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'update':
            permission_classes = [UserIsModeratorPermission | IsOwnerPermission]
        elif self.action == 'destroy':
            permission_classes = [UserIsStaffPermission | IsOwnerPermission]
        else:
            permission_classes = [IsAuthenticated, IsOwnerPermission]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return super().create(*args, **kwargs)




class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission | UserIsModeratorPermission]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission | UserIsModeratorPermission]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, UserIsModeratorPermission | IsOwnerPermission]

class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, UserIsStaffPermission | IsOwnerPermission]