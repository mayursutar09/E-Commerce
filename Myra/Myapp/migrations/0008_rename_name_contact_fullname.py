# Generated by Django 4.0.4 on 2022-06-18 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0007_alter_contact_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='fullname',
        ),
    ]
