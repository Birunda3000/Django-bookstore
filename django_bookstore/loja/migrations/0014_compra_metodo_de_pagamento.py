# Generated by Django 3.1.5 on 2021-02-13 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0013_auto_20210212_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='metodo_de_pagamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='loja.forma_de_pagamento'),
            preserve_default=False,
        ),
    ]
