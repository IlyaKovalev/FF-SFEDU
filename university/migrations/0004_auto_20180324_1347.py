# Generated by Django 2.0.2 on 2018-03-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_auto_20180324_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplines',
            name='discipline',
            field=models.CharField(max_length=500),
        ),
    ]
