# Generated by Django 3.2.6 on 2021-09-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='user_type',
            field=models.BooleanField(default=False),
        ),
    ]
