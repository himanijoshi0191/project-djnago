# Generated by Django 3.1.7 on 2021-03-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_class', '0006_auto_20210322_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
