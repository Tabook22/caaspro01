# Generated by Django 2.2.5 on 2019-09-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peertotur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peertoturfile',
            name='filepath',
            field=models.FileField(blank=True, null=True, upload_to='peertoturs/uploads/', verbose_name=''),
        ),
    ]
