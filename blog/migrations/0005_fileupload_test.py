# Generated by Django 3.2.16 on 2022-11-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='test',
            field=models.CharField(max_length=200, null=True),
        ),
    ]