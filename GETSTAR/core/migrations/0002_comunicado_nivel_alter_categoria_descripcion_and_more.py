# Generated by Django 4.2.1 on 2023-06-05 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicado',
            name='nivel',
            field=models.CharField(blank=True, choices=[('GEN', 'General'), ('PRE', 'Ciclo Preescolar'), ('BAS', 'Ciclo Basico'), ('MED', 'Ciclo Medio')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.TextField(verbose_name='Nombre'),
        ),
    ]
