# Generated by Django 4.1.7 on 2023-03-25 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("djangogp", "0002_alter_standings_options_alter_rider_placeofbirth"),
    ]

    operations = [
        migrations.RenameField(
            model_name="race",
            old_name="wheather",
            new_name="weather",
        ),
    ]
