# Generated by Django 4.0.7 on 2022-08-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(default='dsdsds'),
            preserve_default=False,
        ),
    ]