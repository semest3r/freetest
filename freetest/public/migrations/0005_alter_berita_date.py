# Generated by Django 4.0.1 on 2022-01-28 08:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_alter_berita_tumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]