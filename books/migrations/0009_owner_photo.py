# Generated by Django 3.2.7 on 2021-11-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_owner_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='photo',
            field=models.ImageField(default=1, upload_to='owners_images'),
            preserve_default=False,
        ),
    ]
