# Generated by Django 4.1.7 on 2023-02-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="dob",
            field=models.DateField(verbose_name="date of birth"),
        ),
    ]
