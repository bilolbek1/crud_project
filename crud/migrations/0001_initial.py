# Generated by Django 4.2.5 on 2023-09-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=54)),
                ('b_date', models.DateField()),
                ('job', models.CharField(max_length=32)),
            ],
        ),
    ]