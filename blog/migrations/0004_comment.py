# Generated by Django 2.2.4 on 2019-08-19 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_ptime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=10)),
                ('postedby', models.CharField(max_length=20)),
                ('comment', models.TextField()),
            ],
        ),
    ]
