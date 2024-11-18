from rest_framework import serializers

from school.models import Course, Lesson
from school.validators import LessonLinkValidator
from subscription.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LessonLinkValidator("video_link")]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        lessons = instance.lessons.all()

        if lessons:
            return len(lessons)
        return 0

    def get_subscription(self, instance):
        sub = instance.subscriptions.filter(user=self.context['request'].user)
        if sub:
            return "Subscribed"
        else:
            return "Not Subscribed"


