# Generated by Django 3.2.16 on 2022-11-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_room_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenity',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='amenity',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(to='blog.Amenity'),
        ),
        migrations.AddField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
