# Generated by Django 4.1.7 on 2023-04-02 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("djangogp", "0005_remove_standings_position_alter_result_points"),
    ]

    operations = [
        migrations.AlterField(
            model_name="standings",
            name="rider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="djangogp.rider"
            ),
        ),
    ]
