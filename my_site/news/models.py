from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Наименование категорий")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(verbose_name="Контент")
    photo = models.ImageField(upload_to='photo/%y/%m/%d', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(verbose_name='Публикация')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


