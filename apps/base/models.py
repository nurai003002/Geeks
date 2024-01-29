from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    image = models.ImageField(
        upload_to="portrait/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name="Настройки сайта"
        verbose_name_plural="Настройки сайта"

class Project(models.Model):
    amount = models.CharField(
        max_length = 255,
        verbose_name = 'Количество'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название '
    )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
class Advantages(models.Model):
    image = models.ImageField(
        upload_to='image_adventages/',
        verbose_name='Фотография'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'

class Partner(models.Model):
    image = models.ImageField(
        upload_to='image_partner/',
        verbose_name='Фотография'
    )

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

