from django.db import models

# Create your models here.
class Comments(models.Model):
    content = models.TextField(blank=True, verbose_name='Текст')
    rate = models.PositiveSmallIntegerField(verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    bar = models.ForeignKey('Bars.Bars', on_delete=models.PROTECT, null=True)

    #def __str__(self):
    #    return self.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-rate']
