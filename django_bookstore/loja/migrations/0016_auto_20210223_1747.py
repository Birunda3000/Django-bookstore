# Generated by Django 3.1.7 on 2021-02-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0015_auto_20210223_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='estado_da_compra',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Confirmado', 'Confirmado'), ('Enviado', 'Enviado'), ('Entregue', 'Entregue')], default='Pendente', max_length=10),
        ),
    ]
