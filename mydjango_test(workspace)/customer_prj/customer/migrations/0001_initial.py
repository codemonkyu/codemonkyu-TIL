# Generated by Django 3.1.13 on 2022-02-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('text', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.BooleanField()),
            ],
        ),
    ]
