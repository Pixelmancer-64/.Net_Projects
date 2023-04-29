# Generated by Django 3.2.17 on 2023-02-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('subtitulo', models.CharField(max_length=64)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('local', models.CharField(max_length=128)),
                ('google_maps', models.URLField()),
                ('idade_minima', models.IntegerField(blank=True, null=True, verbose_name='Idade mínima')),
                ('idade_maxima', models.IntegerField(blank=True, null=True, verbose_name='Idade máxima')),
                ('banner_img', models.ImageField(upload_to='banner_evento', verbose_name='Arte do evento')),
                ('is_destaque', models.BooleanField(default=False)),
            ],
        ),
    ]