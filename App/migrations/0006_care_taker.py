# Generated by Django 3.2.12 on 2022-03-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Care_Taker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('DOB', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=50)),
                ('pin_code', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]
