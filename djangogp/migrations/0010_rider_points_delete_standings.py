# Generated by Django 4.1.7 on 2023-04-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangogp", "0009_alter_race_trackcondition_alter_race_weather"),
    ]

    operations = [
        migrations.AddField(
            model_name="rider",
            name="points",
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name="Standings",
        ),
    ]