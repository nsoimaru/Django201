# Generated by Django 4.0.3 on 2022-03-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
