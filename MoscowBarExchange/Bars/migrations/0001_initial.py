# Generated by Django 3.2.13 on 2022-07-03 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('sum_rate', models.PositiveSmallIntegerField()),
                ('address', models.CharField(max_length=150)),
                ('work_time', models.CharField(max_length=150)),
                ('average_check', models.PositiveSmallIntegerField()),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
