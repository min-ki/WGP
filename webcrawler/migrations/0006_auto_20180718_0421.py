# Generated by Django 2.0.7 on 2018-07-18 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawler', '0005_auto_20180715_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='certification_type',
            field=models.CharField(blank=True, choices=[('인필교', '인필교'), ('인선교', '인선교'), ('인선전', '인선전'), ('인필전', '인필전'), ('인필BSM', '인필BSM')], max_length=25),
        ),
    ]
