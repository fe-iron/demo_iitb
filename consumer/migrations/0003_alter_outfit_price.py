# Generated by Django 3.2.5 on 2021-07-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0002_auto_20210710_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='price',
            field=models.IntegerField(default='NaN', null=True),
        ),
    ]