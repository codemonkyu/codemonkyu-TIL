# Generated by Django 3.1.13 on 2022-02-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20220215_0251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Join_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='text',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
