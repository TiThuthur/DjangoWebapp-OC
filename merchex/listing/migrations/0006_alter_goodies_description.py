# Generated by Django 3.2.9 on 2022-05-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0005_auto_20220513_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodies',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]