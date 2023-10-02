from django.db import models

from DjangoTaskApp.models.post import Post


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        verbose_name="Пост"
    )
    text = models.TextField(
        verbose_name="Текст"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.text[:20]}..."

    class Meta:
        ordering = ("date", )
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
