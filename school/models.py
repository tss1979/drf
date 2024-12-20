from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=135, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель', **NULLABLE)
    price = models.ImageField(verbose_name='цена', **NULLABLE)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=135, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    video_link = models.CharField(max_length=135, verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', related_name='lessons')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель', **NULLABLE)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.title
