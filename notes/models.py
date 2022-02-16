from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, 
                             db_index=True,
                             verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Note(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заметка')
    description = models.TextField(default=None, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    changed = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, 
                                 verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-created']
