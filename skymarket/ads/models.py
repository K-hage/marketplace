from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название товара',
        help_text='Введите название товара'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена товара',
        help_text='Укажите цену товара'
    )
    description = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Опишите товар'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ads',
        verbose_name='Автор',
        help_text='Укажите автора'
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="фото",
        help_text="Разместите фото для объявления",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)


class Comment(models.Model):
    text = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Текст комментария',
        help_text='Введите текст комментария'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text='Укажите автора'
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Объявление',
        help_text='Объявление, к которому относится комментарий'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at",)
