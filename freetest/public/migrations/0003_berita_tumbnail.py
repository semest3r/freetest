# Generated by Django 4.0.1 on 2022-01-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_berita_alter_contact_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='tumbnail',
            field=models.ImageField(default='img.png', upload_to='berita'),
        ),
    ]
