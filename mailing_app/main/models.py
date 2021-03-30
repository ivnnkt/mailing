from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserMails(models.Model):
    """модель для хранения email адресов пользователя от лица
    которых он может отправлять рассылки
    """
    user_mail = models.EmailField(
        verbose_name="Email",
        blank=False
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    """Модель Профиль пользователя - расширяет стандартную модель User,
    позволяет хранить различные email адреса пользователя от имени
    которых будут осуществляться рассылки
    (например рабочая и личная почта).

    Email -- email адрес который будет указан в графе From/отправитель
    таких адресов у пользователя может быть несколько.
    Имя -- имя пользователя максимум 50 символов.
    Фамилия -- фамилия пользователя максимум 50 символов.
    """
    name = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    mail_address = models.ManyToManyField(
        UserMails,
        verbose_name="Email",
    )

    def __str__(self):
        return self.name.username


class Addressees(models.Model):
    """Модель Адресаты - содержит информацию об адресатах рассылки.

    Имя -- имя адресата максимум 50 символов.
    Фамилия -- фамилия адресата максимум 50 символов.
    Email -- адрес на который будет отправленно письмо.
    Группа -- какой-либо идентификатор необходимый для фильтрации
    при создании рассылки, например 'College', 'Family'.
    Поле не может быть пустым максимум 100 символов.
    owner -- добавляется автоматически, что бы ограничить доступ
    к адресатам только для теч кто их завел в базу.
    """
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    email = models.EmailField(
        verbose_name="Email",
        blank=False
    )
    group = models.CharField(
        verbose_name="Группа",
        max_length=100,
        blank=False
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    add = models.BooleanField(
        default=False,
        verbose_name='добавить в рассылку'
    )


class Mailing(models.Model):
    """модель Рассылки - конфигурирует рассылку

    """
    name = models.CharField(
        verbose_name="Название рассылки",
        max_length=250
    )
    # letter = models. Шаблон письма поле будет хранить шаблон отправляемого сообщения,
    # необходимо продумать  этот момент может даже завести под это дополнительную таблицу.
    addressees = models.ManyToManyField(Addressees)
    add = models.BooleanField(
        default=True,
        verbose_name='Добавлен'
    )
    mail_from = models.ManyToManyField(Profile)


class Letter(models.Model):
    """модель Письмо - для конфигурации обраца письма для отправки
    """
    name = models.CharField(
        verbose_name="Название письма",
        max_length=250
    )
    content = models.TextField(verbose_name="Содержание письма", blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to='static/main/images')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """По сигналу о сохрании нового пользователя автоматически создает
    профаил пользователя.
    """
    if created:
        Profile.objects.get_or_create(name=instance)