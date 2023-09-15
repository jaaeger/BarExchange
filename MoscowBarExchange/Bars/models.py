from django.db import models

# Create your models here.
class Bars(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    sum_rate = models.PositiveSmallIntegerField(verbose_name='Рейтинг')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    work_time = models.CharField(max_length=150, verbose_name='Время работы')
    average_check = models.PositiveSmallIntegerField(verbose_name='Средний чек')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бар'
        verbose_name_plural = 'Бары'
        ordering = ['-sum_rate']
