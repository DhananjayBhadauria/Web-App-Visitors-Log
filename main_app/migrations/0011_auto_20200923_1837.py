# Generated by Django 3.1 on 2020-09-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20200923_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='/unnamed.jpg', null=True, upload_to='ClientProfilePics/'),
        ),
    ]