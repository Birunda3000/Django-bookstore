# Generated by Django 3.1.5 on 2021-01-21 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20210121_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.editora'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.genero'),
        ),
    ]