from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   

# новая группа пользователей
group, created = Group.objects.get_or_create(name='Полный доступ')

# получаем рутправа
content_type = ContentType.objects.get_for_model(User)
permissions = Permission.objects.filter(content_type=content_type)

# добавляем права группе
for permission in permissions:
    group.permissions.add(permission)