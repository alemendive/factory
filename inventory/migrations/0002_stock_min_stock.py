# Generated by Django 3.0.7 on 2024-10-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='min_stock',
            field=models.IntegerField(default=0),
        ),
    ]