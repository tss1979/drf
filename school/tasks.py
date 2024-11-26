from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils import timezone

from config import settings
from school.models import Course
from subscription.models import Subscription
from users.models import User


@shared_task
def send_course_notification(course_pk):
    subscriptions = Subscription.objects.filter(course_id=course_pk)
    course = get_object_or_404(Course, pk=course_pk)
    mails = [sub.user.email for sub in subscriptions]
    send_mail(
        subject="Обновление курса",
        message=f"Обновление курса {course}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=mails
    )


@shared_task
def change_user_status():
    today = timezone.now().today()
    users = User.objects.all()
    for user in users:
        if user.last_login:
            if not user.is_staff and (today - user.last_login).days > 30:
                user.is_active = False
                user.save()
