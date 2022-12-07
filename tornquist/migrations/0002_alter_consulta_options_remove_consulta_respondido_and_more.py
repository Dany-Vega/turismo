# Generated by Django 4.1.2 on 2022-12-04 23:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
import tornquist.validaciones


class Migration(migrations.Migration):

    dependencies = [
        ('tornquist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consulta',
            options={},
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='respondido',
        ),
        migrations.AddField(
            model_name='consulta',
            name='estado_respuesta',
            field=models.CharField(blank=True, choices=[('Contestada', 'Contestada'), ('No Contestada', 'No Contestada'), ('En proceso', 'En proceso')], default='No Contestada', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='asunto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='mensaje',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[tornquist.validaciones.solo_caracteres], verbose_name='Nombre Completo'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='telefono',
            field=models.IntegerField(blank=True, max_length=50, null=True, verbose_name='Numero de telefono'),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField()),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('consulta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tornquist.consulta')),
            ],
        ),
    ]