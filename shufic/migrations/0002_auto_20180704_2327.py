# Generated by Django 2.0.6 on 2018-07-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shufic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='Video_likes',
            field=models.IntegerField(default=0),
        ),
    ]
