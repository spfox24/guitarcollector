# Generated by Django 3.1.6 on 2021-02-18 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210217_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='cases',
            field=models.ManyToManyField(to='main_app.Case'),
        ),
    ]