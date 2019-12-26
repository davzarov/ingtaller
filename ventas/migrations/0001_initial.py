# Generated by Django 2.1.15 on 2019-12-26 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1, verbose_name='cantidad')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recibido', models.IntegerField(default=0, verbose_name='recibido')),
                ('vuelto', models.IntegerField(blank=True, default=0, verbose_name='vuelto')),
                ('total', models.IntegerField(default=0, verbose_name='total')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='modificado')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ventas.Venta'),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('venta', 'producto')},
        ),
    ]
