# Generated by Django 3.2 on 2021-07-28 04:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_alter_photo_profile_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='bakhood',
            name='bak_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='bak_pics'),
            preserve_default=False,
        ),
    ]
