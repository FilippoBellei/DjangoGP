# Generated by Django 4.1.7 on 2023-03-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangogp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="standings",
            options={"verbose_name_plural": "Standings"},
        ),
        migrations.AlterField(
            model_name="rider",
            name="placeOfBirth",
            field=models.CharField(max_length=255),
        ),
    ]
