import re
from rest_framework.serializers import ValidationError


class LessonLinkValidator:

    def  __init__(self, field):
        self.field = field

    def __call__(self, link):
        if link:
            reg = re.compile(r'^https:\/\/www.youtube.com\/watch\?.+$')
            value = dict(link).get(self.field)
            if not bool(reg.match(value)):
                raise ValidationError("Не принимаются ссылки кроме ссылок на ресурс youtube")

