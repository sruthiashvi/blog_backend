# Generated by Django 2.2.4 on 2019-08-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pid',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='comment',
            name='postedby',
            field=models.CharField(max_length=25),
        ),
    ]