# Generated by Django 4.0.1 on 2022-01-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_alter_berita_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
