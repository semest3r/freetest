# Generated by Django 4.0.1 on 2022-01-31 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0008_question_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='pertanyan',
            new_name='pertanyaan',
        ),
    ]
