# Generated by Django 3.1 on 2020-08-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Submission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='question_4',
            field=models.CharField(choices=[('Option A', 'Option A'), ('Option B', 'Option B'), ('Option C', 'Option C'), ('Option D', 'Option D')], default='', max_length=100),
        ),
    ]
