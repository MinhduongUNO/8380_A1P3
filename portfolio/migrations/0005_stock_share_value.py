# Generated by Django 2.0.5 on 2018-07-19 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_investment_result_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='share_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]