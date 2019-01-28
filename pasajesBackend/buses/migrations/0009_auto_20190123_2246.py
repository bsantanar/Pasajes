# Generated by Django 2.1.5 on 2019-01-23 22:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0008_bus_chofer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partida', models.DateTimeField(verbose_name='partida')),
                ('llegada', models.DateTimeField(verbose_name='llegada')),
                ('buses', models.ManyToManyField(to='buses.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Trayecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
                ('creado', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='creado')),
                ('modificado', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='modificado')),
            ],
        ),
        migrations.AddField(
            model_name='horario',
            name='trayecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='buses.Trayecto'),
        ),
    ]
