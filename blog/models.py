from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from django.contrib.auth.models import User


def gen_slug(s):  # todo перевод с кирилицы на латиницу
    """функция для генерации поля slug при создании экземпляра post"""
    new_slug = slugify(s, allow_unicode=False)  # allow_unicode=True - позволяет использовать кирилицу
    return new_slug + '-' + str(int(time()))   # для уникальности добавляем время


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(max_length=10000)
    tags = models.ManyToManyField('Tag', related_name='posts')  # posts вместо _set
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        """перенаправляет на указанный url с подстановкой аргументов"""
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """переопределение род. метода для автоматической генерации  поля slug из поля title
        при создании(не изменении) поста"""
        if not self.id:  # если экземпляр не имеет id - тоесть его еще нет в базе
            self.slug = gen_slug(self.title)  # тогда генерируем slug из названия поста(title)
        super().save(*args, **kwargs)

    # def get_update_url(self):
    #     """перенаправляет на указанный URL с подстановкой аргумента slug
    #     чтобы не писать в шаблоне {% url 'tag_update_url' slug=tag.slug %}"""
    #     return reverse('post_update_url', kwargs={'slug': self.slug})
    #
    # def get_delete_url(self):
    #     return reverse('post_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,)

    class Meta:
        ordering = ['title']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        """перенаправляет на указанный url с подстановкой аргументов"""
        return reverse('tag_detail', kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     """перенаправляет на указанный URL с подстановкой аргумента slug
    #     чтоб вместо {% url 'tag_update_url' slug=tag.slug %} писать {{ tag.get_update_url }}"""
    #     return reverse('tag_update_url', kwargs={'slug': self.slug})
    #
    # def get_delete_url(self):
    #     return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class PostComment(models.Model):
    """Model representing a comment against a blog post."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.TextField(max_length=1000)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        """String for representing the Model object"""
        len_title = 75
        if len(self.comment) > len_title:
            string = self.comment[:len_title] + '...'
        else:
            string = self.comment
        return "{}. {}".format(self.post_date, string)

