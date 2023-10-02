from django.db import models


class Post(models.Model):
    title = models.TextField(
        verbose_name="Заголовок"
    )
    text = models.TextField(
        verbose_name="Текст"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    likes = models.IntegerField(
        default=0,
        verbose_name="Лайки"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("date", )
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
