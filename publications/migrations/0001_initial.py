# Generated by Django 3.1.3 on 2020-11-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст публикации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='publication_pictures', verbose_name='Картинка публикации')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
