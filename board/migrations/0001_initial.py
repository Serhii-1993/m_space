# Generated by Django 4.2.6 on 2023-10-30 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Назва', max_length=150, verbose_name='Назва')),
                ('description', models.TextField(help_text='Опис', verbose_name='Опис')),
                ('board_img', models.ImageField(upload_to='board_img/', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Ціна')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опублікувати')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(db_index=True, max_length=100)),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Додай коментар')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.board')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='board.comments')),
            ],
        ),
    ]
