# Generated by Django 2.2.5 on 2019-09-10 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peertotur', '0002_auto_20190910_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peertoturfile',
            name='pname',
        ),
    ]