# Generated by Django 2.2.7 on 2019-11-13 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('employee_name', models.TextField(default='Enter your name', max_length=30)),
                ('employee_salary', models.IntegerField(blank=True, default=100000000)),
                ('employee_age', models.IntegerField()),
                ('profile_image', models.URLField(blank=True, default='Enter the path of the pic')),
            ],
        ),
    ]
