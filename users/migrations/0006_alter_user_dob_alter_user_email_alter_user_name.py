# Generated by Django 4.1.7 on 2023-03-07 09:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_user_is_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="dob",
            field=models.DateField(verbose_name="Date Of Birth"),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=200, verbose_name="Full Name"),
        ),
    ]
