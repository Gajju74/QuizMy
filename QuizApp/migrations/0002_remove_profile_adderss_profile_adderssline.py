# Generated by Django 4.0.3 on 2022-03-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Adderss',
        ),
        migrations.AddField(
            model_name='profile',
            name='Adderssline',
            field=models.CharField(default='', max_length=150),
        ),
    ]