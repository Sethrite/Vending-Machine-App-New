# Generated by Django 5.1.2 on 2024-10-21 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snackspot',
            old_name='machine',
            new_name='Machine',
        ),
        migrations.AddField(
            model_name='snackspot',
            name='snack',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
