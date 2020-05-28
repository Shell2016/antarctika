from django.db import models
from django.forms.widgets import Textarea


class Promo(models.Model):
    title = models.CharField(
        max_length=100, verbose_name='Заголовок страницы', blank=True)
    content_title = models.CharField(
        max_length=100, verbose_name='Заголовок для контента', blank=True)
    content_text = models.TextField(verbose_name='Контент', blank=True)
    footer_text = models.CharField(
        max_length=200, verbose_name='Надпись отцентрованная под контентом', blank=True)

    class Meta:
        verbose_name = 'Акции'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return 'Редактирование страницы Акции'


class PromoItem(models.Model):
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name
