# Generated by Django 4.1 on 2022-08-05 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarioAtividades', '0004_tabela_criada_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='duracao',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='tabela',
            name='mes',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
    ]
