# Generated by Django 2.2 on 2019-04-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bracketitem',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
