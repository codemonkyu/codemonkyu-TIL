# Generated by Django 3.1.13 on 2022-02-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord', '0005_auto_20220220_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]