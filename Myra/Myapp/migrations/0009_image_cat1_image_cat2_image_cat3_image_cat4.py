# Generated by Django 4.0.4 on 2022-07-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0008_rename_name_contact_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cat1',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='cat2',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='cat3',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='cat4',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
