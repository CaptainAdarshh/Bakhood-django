# Generated by Django 3.2 on 2021-07-28 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20210728_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakhood',
            name='bak_pic',
            field=models.ImageField(blank=True, upload_to='bak_pics'),
        ),
    ]