# Generated by Django 2.1.7 on 2019-03-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20190312_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(max_length=120),
        ),
    ]