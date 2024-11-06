from rest_framework import serializers

from school.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        lessons = instance.lessons.all()

        if lessons:
            return len(lessons)
        return 0


