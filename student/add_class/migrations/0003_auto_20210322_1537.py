# Generated by Django 3.1.7 on 2021-03-22 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_class', '0002_auto_20210322_1501'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentinfo',
            unique_together=set(),
        ),
        migrations.AlterModelTable(
            name='studentinfo',
            table='student_data',
        ),
    ]
