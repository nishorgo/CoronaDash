# Generated by Django 4.2.1 on 2023-05-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_remove_symptomguideline_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptomguideline',
            name='display_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
