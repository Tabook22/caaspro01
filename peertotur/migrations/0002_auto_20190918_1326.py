# Generated by Django 2.2.5 on 2019-09-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peertotur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peertotur',
            name='paddress',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='pdep',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='pemail',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='E-mail address'),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='pgpacum',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Cumulative GPA'),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='pgpamajor',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='GPA in major'),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='pgsm',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='GSM'),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='pmajor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Major'),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='pname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='ptel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tel'),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='reqdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='peertotur',
            name='yearofstudy',
            field=models.CharField(blank=True, choices=[('Soph', 'Sopph'), ('Jr', 'Jr'), ('Sr', 'Sr'), ('Grad_Student', 'Grad_Student')], max_length=20, null=True, verbose_name='Year of Study'),
        ),
    ]