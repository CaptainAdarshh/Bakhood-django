# Generated by Django 3.2 on 2021-07-28 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20210728_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics/'),
        ),
    ]
