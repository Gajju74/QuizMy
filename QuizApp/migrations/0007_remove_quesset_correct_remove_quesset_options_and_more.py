# Generated by Django 4.0.1 on 2022-04-02 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0006_quesset_datecreated_quesset_lastupdated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quesset',
            name='Correct',
        ),
        migrations.RemoveField(
            model_name='quesset',
            name='Options',
        ),
        migrations.RemoveField(
            model_name='quesset',
            name='Point',
        ),
        migrations.RemoveField(
            model_name='quesset',
            name='Question',
        ),
        migrations.CreateModel(
            name='OptionSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=255)),
                ('Options', models.TextField(max_length=255)),
                ('Correct', models.CharField(max_length=4)),
                ('Point', models.IntegerField()),
                ('DateCreated', models.DateTimeField(auto_now_add=True)),
                ('LastUpdated', models.DateTimeField(auto_now=True)),
                ('QuesSet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizApp.category')),
            ],
            options={
                'db_table': 'optionset',
            },
        ),
    ]
