# Generated by Django 3.1 on 2020-08-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20200817_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subs',
            name='question_1',
            field=models.CharField(choices=[('Choose', 'Choose'), ('Option A', 'Option A'), ('Option B', 'Option B'), ('Option C', 'Option C'), ('Option D', 'Option D')], default='', max_length=100),
        ),
    ]