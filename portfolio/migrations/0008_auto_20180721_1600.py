# Generated by Django 2.0.5 on 2018-07-21 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20180721_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='purchase_value',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='share_value',
        ),
    ]
