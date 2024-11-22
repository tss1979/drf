from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from school.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}
METHODS = (('c', 'cash'), ('cd', 'card'), ('tf', 'transfer'))


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(verbose_name='автар', **NULLABLE)
    city = models.CharField(max_length=55, verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name="payments")
    payment_date = models.DateTimeField(verbose_name='дата оплаты', default=datetime.now())
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', related_name="course", **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', related_name="lesson", **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=2, choices=METHODS, verbose_name='метод оплаты')
    session_id = models.CharField(max_length=255, **NULLABLE, verbose_name='id сессии')
    link = models.URLField(max_length=400, **NULLABLE, verbose_name='ссылка на оплату')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return f'{self.user} - {self.amount}'
