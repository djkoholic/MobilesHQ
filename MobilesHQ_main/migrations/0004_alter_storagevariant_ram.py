# Generated by Django 3.2.5 on 2021-09-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MobilesHQ_main', '0003_rename_title_product_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagevariant',
            name='ram',
            field=models.IntegerField(blank=True),
        ),
    ]
