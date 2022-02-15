from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="URL", max_length=20)
    description = models. TextField(verbose_name="Описание")

    # Metadata
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name="Текст поста")
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Дата публикации")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name='posts', Убрать по просьбе ревьера, а на хрена
        # убрать не понятно, он не пояснил!
        verbose_name="Автор"
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='groups',
        blank=True,
        null=True)
# Metadata

    def __str__(self):
        # выводим текст поста
        return self.text
