# Generated by Django 4.2.7 on 2023-11-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='task_images/'),
        ),
    ]
