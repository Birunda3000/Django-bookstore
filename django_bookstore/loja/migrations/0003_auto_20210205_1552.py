# Generated by Django 3.1.5 on 2021-02-05 18:52

from django.db import migrations, models
import loja.models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20210205_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True, validators=[loja.models.validate_interval_age]),
        ),
    ]
