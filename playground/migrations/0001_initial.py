# Generated by Django 5.1.2 on 2024-10-21 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VendingMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SnackSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.TextField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.vendingmachine')),
            ],
        ),
    ]
