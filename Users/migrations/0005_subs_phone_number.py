# Generated by Django 3.1 on 2020-08-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20200817_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='subs',
            name='phone_number',
            field=models.CharField(default='', max_length=200),
        ),
    ]