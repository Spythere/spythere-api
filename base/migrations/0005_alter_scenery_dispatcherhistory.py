# Generated by Django 4.0 on 2021-12-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_scenery_currentdispatcherid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenery',
            name='dispatcherHistory',
            field=models.JSONField(default=dict),
        ),
    ]