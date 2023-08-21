from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import MAX_LENGTH_TEXT

User = get_user_model()


class Post(models.Model):
    text = models.TextField("Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    image = models.ImageField(
        "Изображение", upload_to="posts/", null=True, blank=True
    )
    group = models.ForeignKey(
        "Group",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Группа",
        related_name="groups",
    )

    def __str__(self):
        return self.text[:MAX_LENGTH_TEXT]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="Пост",
    )
    text = models.TextField("Текст")
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )

    class Meta:
        default_related_name = "comments"

    def __str__(self):
        return self.text[:MAX_LENGTH_TEXT]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="Подписчик",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="автор",
    )


class Group(models.Model):
    title = models.CharField("Название", max_length=256)
    slug = models.SlugField("Слаг", unique=True)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title[:MAX_LENGTH_TEXT]
