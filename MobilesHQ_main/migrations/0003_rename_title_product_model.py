# Generated by Django 3.2.5 on 2021-09-16 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MobilesHQ_main', '0002_colorvariant_product_storagevariant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='model',
        ),
    ]
