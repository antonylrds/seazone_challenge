# Generated by Django 4.2.5 on 2023-09-22 19:49

from django.db import migrations, models
import reservations.utils


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default=reservations.utils.generate_random_string, editable=False, max_length=8),
        ),
    ]
