# Generated by Django 2.2.5 on 2019-09-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peertotur', '0005_auto_20190915_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peertotur',
            name='pexgraduate',
            field=models.DateField(blank=True, verbose_name='Expected date of Graduation (mm/dd/YYYY)'),
        ),
    ]
