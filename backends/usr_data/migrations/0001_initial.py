# Generated by Django 4.2.9 on 2024-01-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="usr_data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("device_id", models.CharField(max_length=100)),
                ("x", models.FloatField()),
                ("y", models.FloatField()),
                ("altitude", models.FloatField()),
                ("x_speed", models.FloatField()),
                ("y_speed", models.FloatField()),
                ("z_speed", models.FloatField()),
                ("posture", models.CharField(max_length=100)),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "usr_data",
            },
        ),
    ]