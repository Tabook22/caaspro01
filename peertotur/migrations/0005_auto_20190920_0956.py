# Generated by Django 2.2.5 on 2019-09-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peertotur', '0004_auto_20190919_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peertotur',
            name='pimg',
            field=models.ImageField(blank=True, null=True, upload_to='peertoturs/img/%Y/%m/%d', verbose_name='Peer Totur Image'),
        ),
    ]
