# Generated by Django 4.2.1 on 2023-06-05 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_comunicado_nivel_alter_categoria_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AddField(
            model_name='comunicado',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
        migrations.AlterModelTable(
            name='categoria',
            table='categoria',
        ),
    ]
