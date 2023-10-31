from datetime import date

from django.db import models
from user.models import User

class Board(models.Model):

    title = models.CharField('Назва', help_text='Назва', max_length=150)
    description = models.TextField('Опис', help_text='Опис')
    board_img = models.ImageField('Фото', upload_to='board_img/')
    price = models.DecimalField('Ціна', max_digits=15, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категорія', null=True)
    create_date = models.DateTimeField('Дата створення', auto_now_add=True)
    update_date = models.DateTimeField('Дата оновлення', auto_now=True)
    is_published = models.BooleanField('Опублікувати', default=False)


    def str(self):
        return self.title

    class Meta:
        ordering = ['-create_date']


class Category(models.Model):

    cat_name = models.CharField(max_length=100, db_index=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.cat_name


class Comments(models.Model):

    text = models.TextField(help_text='Додай коментар')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Назви себе')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.user.username}: {self.text}'
