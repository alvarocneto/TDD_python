# Generated by Django 2.0.2 on 2018-03-20 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_item_list'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]
