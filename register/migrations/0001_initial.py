# Generated by Django 4.1.3 on 2022-11-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "user_id",
                    models.IntegerField(
                        auto_created=True,
                        blank=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="pk",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=25, unique=True, verbose_name="username"
                    ),
                ),
            ],
        ),
    ]