# Generated by Django 4.2.6 on 2023-11-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alphamain', '0013_remove_product_member3_remove_product_roll3'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperpresentation',
            name='contact',
            field=models.CharField(default='sample', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectpresentation',
            name='contact',
            field=models.CharField(default='lkj', max_length=20),
            preserve_default=False,
        ),
    ]