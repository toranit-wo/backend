# Generated by Django 3.2.3 on 2021-06-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingponghit', '0003_remove_pingponghit_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='pingponghit',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
