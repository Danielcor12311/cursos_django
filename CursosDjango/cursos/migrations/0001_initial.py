# Generated by Django 5.0.6 on 2025-06-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('nivel', models.CharField(max_length=15)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fecha_inicio', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografia')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
