# Generated by Django 4.1 on 2022-08-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarioAtividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtabela',
            name='atividades',
            field=models.ManyToManyField(related_name='itens', to='diarioAtividades.atividade'),
        ),
    ]